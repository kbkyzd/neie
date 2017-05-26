<p align="center"><img src="https://raw.githubusercontent.com/kbkyzd/eien/master/public/img/KBKYZDx600.png"></p>

<p align="center">neie</p>

## Core Dependencies
* Python 2.7
* arrow
* requests


## Development
Just run `pip install -r requirements.txt`. The GrovePi library is crazy outdated and most of them aren't even versioned/available on pip, so `requirements.txt` barely has anything.

Most of the stuff barely even works if you're using a regular raspbian image. You should use [their](https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/) version of raspbian to get all the core dependencies pre-installed.

Don't bother with Python 3 or virtualenv.

## Configuration
All configuration is done through dotenv. Copy `.example.env` to `.env` and fill in the values. They should be pretty self explantory. For `TEMP_SENSOR_TYPE`, see [the repo](https://github.com/DexterInd/GrovePi/blob/master/Projects/Home_Weather_Display/Home_Weather_Display.py). Basically, if you're using the GrovePi, leave it at `0`.

`EIENKEY` is the api token key (it's whatever's that set on the `users` table on the DB. If you've seeded the database, you'll only need to fill in `kappa`.

`settings.py` is the actual "configuration" file. It parses `.env` and loads the required configuration/secrets into variables. Then, it gets imported into whatever requires these values.

## `arrivals.py`
`arrivals` is basically a very simple script (well, all of them are simple) that sends a request to the API endpoint exposed by `eien`. The output by `eien` is basically identical to the one from datamall (because it is).

## `tempclient.py`
`tempclient` reads in values from the sensor, and `POST`s them to the API endpoint. Pretty simple.