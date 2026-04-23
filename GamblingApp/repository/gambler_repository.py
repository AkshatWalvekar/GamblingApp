from config.db import get_connection

class GamblerRepository:

    def save(self, gambler):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO gamblers 
        (name, email, initial_stake, current_stake, win_threshold, loss_threshold)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            gambler.name,
            gambler.email,
            gambler.initial_stake,
            gambler.current_stake,
            gambler.win_threshold,
            gambler.loss_threshold
        ))

        conn.commit()

    def find_by_id(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM gamblers WHERE id=%s", (gambler_id,))
        return cursor.fetchone()

    def update(self, gambler_id, name, email):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE gamblers SET name=%s, email=%s WHERE id=%s",
            (name, email, gambler_id)
        )
        conn.commit()

    def reset(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE gamblers
            SET current_stake = initial_stake,
                total_bets = 0,
                total_wins = 0,
                total_losses = 0
            WHERE id=%s
        """, (gambler_id,))

        conn.commit()