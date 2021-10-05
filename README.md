# Instagram Follow Bot

This bot can make follow to followers from user account that u will put in input.

##Requirements
```buildoutcfg
python no less than 3.8

chromedriver.exe
# make sure that you use latest version of chromedriver 
# check latest version here https://chromedriver.chromium.org/downloads


```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r /path/to/requirements.txt
```

## You also can run this script
```bash
pip install selenium
```

## Usage
##Your instagram accounts data

```python
#main.py

# user_name = instagram login(phone number, email or instagram nickname)
user_name = 'nickname or email or phone number'

#user_pw = instagram password
user_pw = 'password'

```

##Bot config

```python
#main.py

# fn = instagram account to steal their followers
fn = 'caseit_ua'

#amount_by_hour = amount follows that bot can do by one cycle iteration
amount_by_hour = 30

# amount_by_cycle = amount follows that bot can do by one day
# don't input bigger than 350
amount_by_cycle = 210

```

##Set your config there

```python
#simple_instagrma_bot.py

# Scrollbox Xpath
scroll_box = '/html/body/div[6]/div/div/div[2]'

# Scrollbox quit button Xpath
scroll_box_quit_button = '/html/body/div[6]/div/div/div[1]/div/div[2]/button/div'

#amount pixels for scrollbox distance
amount_of_scrollbox_pixels = '40000'

```


#Bot launch
```bash

python main.py

```


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
