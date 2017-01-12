TRUSTLAB
========
> Web-based multiplayer strategy games and economics experiments to measure **trust**.
> This software is developed with the financial support of the European Research Council
> under the European Community’s Horizon H2020 Program (H2020-ERC-2014-CoG Grant Agreement n° 647870).

![ERC and Sciences Po logos](https://raw.githubusercontent.com/medialab/trustlab/master/_readmefiles/logos.jpg)

### Getting started

**Trustlab** is based on [**oTree**](http://www.otree.org/), a Python, [Django](https://djangoproject.com)-based framework for econn-games. Please refer to the following article regarding oTree:

*[Chen, D.L., Schonger, M., Wickens, C., 2016. oTree - An open-source platform for laboratory, online and field experiments. Journal of Behavioral and Experimental Finance, vol 9: 88-97](http://www.sciencedirect.com/science/article/pii/S2214635016000101)*

**Trustlab** also includes a working version of the [Implicit Association Test](https://implicit.harvard.edu/implicit/education.html), and several changes to the base games it restricts itself to (**Trust**, **Dictator**, **Public Good**)... among other things.

If you're comfortable with the oTree platform, you should be up-to-speed in no time. Nevertheless, there are several idiosyncrasies you should be aware of in order to run Trustlab properly. They are listed below, and in the [Wiki](https://github.com/medialab/trustlab/wiki).

#### Prerequisites
You may want to refer to [oTree's](http://otree.readthedocs.io/en/latest/install.html) installation tutorial. In a nutshell, you need Python 3.5 and `pip`, to be able to install oTree using the latter (`pip3 install -U otree-core`).

It is strongly suggested that you use a [`virtualenv`](https://virtualenv.pypa.io/en/stable/) in order to run your platform in the best possible way. If you do so, you should follow this [tutorial]() to know how to set up the necessary environment variables for your instance of Trustlab.

#### Installing
- Clone this directory:

```bash
git clone git@github.com:medialab/trustlab.git
```

- Install the dependencies:

```bash
pip install -r requirements_base.txt
```

- Set up the necessary environment variables ([see how-to for `virtualenv`]()):

```bash
export OTREE_SECRET_KEY=...
export OTREE_ADMIN_PASSWORD=...
export OTREE_PRODUCTION=False
export OTREE_ADMIN_PASSWORD=...
export OTREE_SECRET_KEY=...
export OTREE_AUTH_LEVEL=STUDY
export OTREE_LANGUAGE_CODE=...
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

- Reset your DB to run the migrations. From the console at the root of your project:

```bash
otree resetdb
```

- If your `OTREE_PRODUCTION` setting is setting to `True`, build the static assets:

```bash
otree exportstatic
```

- Run the server.

```bash
otree runserver
```

- Check out [http://localhost:8000/](http://localhost:8000/), and use the credentials you've registered in your related environment variables to log in.

### Deployment

The Trustlab project has been successfully deployed on an instances of [Heroku](https://heroku.com)'s dynos. Please refer the [server deployment documenation in oTree](http://otree.readthedocs.io/en/latest/server/intro.html) for further information.

Don't forget to set up your environment variables, regardless of the deployment strategy.

### Contributing

Please read [CONTRIBUTING.md](https://github.com/medialab/trustlab/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/medialab/trustlab/tags).

### Authors

 * **Daniel L. Chen, Martin Schonger and Christopher Wickens** - *Initial work on oTree* - [oTree-org](https://github.com/oTree-org)
 * **Davy Peter Braun** - *Initial work on Trustlab, including animated simulations, IAT...* - [dheavy](https://github.com/dheavy)
 * **Paul Girard** - *Overwiew of project* - [paulgirard](https://github.com/paulgirard)

### License

This project is licensed under a modified version of the MIT License, matching that of oTree - see the [LICENSE.md](LICENSE.md) file for details.

### Acknowledgments

* Thanks to Chris Wickens for his help, both in person and on the [oTree newsgroup](groups.google.com/group/otree)
* Hat tip to the oTree community
