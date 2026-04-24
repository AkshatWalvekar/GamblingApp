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

def get_bets_by_gambler(self, gambler_id):
    from config.db import get_connection
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM bets WHERE gambler_id=%s ORDER BY id",
        (gambler_id,)
    )

    return cursor.fetchall()