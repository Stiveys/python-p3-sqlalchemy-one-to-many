import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review, Base

class TestOneToMany:
    @pytest.fixture
    def session(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create test data
        game = Game(
            title="Test Game",
            genre="Test Genre",
            platform="Test Platform",
            price=50
        )
        session.add(game)
        session.commit()

        review = Review(
            score=9,
            comment="Test Comment",
            game_id=game.id
        )
        session.add(review)
        session.commit()

        yield session

        # Clean up
        session.close()

    def test_game_has_reviews(self, session):
        game = session.query(Game).first()
        assert len(game.reviews) > 0
        assert game.reviews[0].score == 9
        assert game.reviews[0].comment == "Test Comment"

    def test_review_belongs_to_game(self, session):
        review = session.query(Review).first()
        assert review.game is not None
        assert review.game.title == "Test Game"