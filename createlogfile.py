# !/usr/bin/python
import datetime
import faker
import numpy
import random
import time


def main():
    """
    Creates sample apache style access files

    This takes approx a minute to write 100k rows
    """

    Faker = faker.Faker()

    writetime = datetime.datetime.now()

    timestr = time.strftime("%Y%m%d-%H%M%S")

    logfilename = 'server1_access_log_' + timestr + '.log'

    f = open(logfilename, 'w')

    actions = ["GET", "POST", "PUT"]

    responses = ["200", "301", "404", "500"]

    pages = ["/", "/apache_pb.gif", "/img/Customers/Cemex.gif", "/img/Customers/Alucobond.gif", "/fonts/flaticon.woff",
             "/img/Customers/Dryvit.gif", "/img/Customers/Euroclad.gif", "/favicon.ico", "/templates/generic.php",
             "/css/setup.css"]

    browsers = [Faker.chrome, Faker.firefox, Faker.internet_explorer, Faker.opera, Faker.safari]

    for i in range(1, 100000):
        increment = datetime.timedelta(seconds=random.randint(1, 30))
        writetime += increment

        ip = Faker.ipv4()
        action = numpy.random.choice(actions, p=[0.7, 0.2, 0.1])
        uri = random.choice(pages)
        size = random.randint(3, 2000)
        response = numpy.random.choice(responses, p=[0.8, 0.05, 0.1, 0.05])
        referer = Faker.uri()
        useragent = numpy.random.choice(browsers, p=[0.5, 0.3, 0.1, 0.05, 0.05])()
        f.write('%s - - [%s %s] "%s %s HTTP/1.0" %s %s "%s"\n' %
                (ip, writetime.strftime('%d/%b/%Y:%H:%M:%S'), action, uri, response, size, referer, useragent))
        f.flush()

    f.close()


if __name__ == '__main__':
    main()
