from config.db import get_connection

class StakeRepository:

    def add_transaction(self, tx):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO stake_transactions 
        (gambler_id, transaction_type, amount, balance_after)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (
            tx.gambler_id,
            tx.transaction_type,
            tx.amount,
            tx.balance_after
        ))

        conn.commit()

    def update_balance(self, gambler_id, new_balance):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE gamblers SET current_stake=%s WHERE id=%s",
            (new_balance, gambler_id)
        )

        conn.commit()

    def get_transactions(self, gambler_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM stake_transactions WHERE gambler_id=%s",
            (gambler_id,)
        )

        return cursor.fetchall()