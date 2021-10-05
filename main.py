'''
    Here u need to put your instagram accounts data
    user_name = login
    user_pw = password
    fn = instagram account to steal their followers
    amount_by_hour = amount follows that bot can do by one cycle iteration
    amount_by_cycle = amount follows taht bot can do by one day

    After do
'''


from simple_instagram_bot import InstaBot


user_name = 'ddddzzzsaad'
user_pw = '1003kv2000'
fn = 'caseit_ua'
amount_by_hour = 30
amount_by_cycle = 210


if __name__ == '__main__':
    ibot = InstaBot(user_name, user_pw, fn, amount_by_hour, amount_by_cycle)
    ibot.get_followers()


