from loguru import logger

from resume_poster import connect


class Resume:
    pass


class RabotaDriver:
    pass


def main():
    conn = connect('emails.db')
    cur = conn.cursor()

    emails = cur.execute('select email from emails where status is NULL').fetchall()
    for email in emails:
        print(email)
        posted = True
        if posted:
            print('posted')


try:
    if __name__ == '__main__':
        main()
except Exception as error:
    logger.exception(error)
