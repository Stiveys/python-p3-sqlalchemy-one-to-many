#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Access the first review instance in the database
    review = session.query(Review).first()
    print("First review:", review)

    # Check if review exists before accessing attributes
    if review:
        # Get the game_id foreign key for the review instance
        print("Review's game_id:", review.game_id)

        # Access the game associated with this review using the relationship
        print("Review's game:", review.game)
    else:
        print("No reviews found in the database. Run seed.py first.")

    # Access the first game instance in the database
    game = session.query(Game).first()
    print("\nFirst game:", game)

    # Check if game exists before accessing attributes
    if game:
        # Access all reviews for this game using the relationship
        print("Game's reviews:")
        for review in game.reviews:
            print(f"- {review}")
    else:
        print("No games found in the database. Run seed.py first.")