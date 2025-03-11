#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review
from faker import Faker

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Review).delete()
    session.query(Game).delete()

    fake = Faker()

    # Create sample games
    games = []
    platforms = ["Switch", "PS5", "Xbox", "PC", "Mobile"]
    genres = ["RPG", "FPS", "Adventure", "Simulation", "Strategy", "Sports"]

    for i in range(5):
        game = Game(
            title=fake.name(),
            platform=fake.random_element(platforms),
            genre=fake.random_element(genres),
            price=fake.random_int(min=10, max=70)
        )
        session.add(game)
        games.append(game)

    session.commit()

    # Create sample reviews
    for game in games:
        # Each game gets 1-3 reviews
        for _ in range(fake.random_int(min=1, max=3)):
            review = Review(
                score=fake.random_int(min=1, max=10),
                comment=fake.sentence(),
                game_id=game.id
            )
            session.add(review)

    session.commit()

    print(f"Database seeded with {len(games)} games and {session.query(Review).count()} reviews!")