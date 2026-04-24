from config.db import get_connection

class BetRepository:

    def save(self, bet):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO bets 
        (gambler_id, bet_amount, win, stake_before, stake_after)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            bet.gambler_id,
            bet.bet_amount,
            bet.win,
            bet.stake_before,
            bet.stake_after
        ))

        conn.commit()