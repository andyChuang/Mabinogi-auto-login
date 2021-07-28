import utils


class AccountList:
    account_infos = None

    def __init__(self, file_path):
        self.account_infos = dict(enumerate(utils.load_json(file_path)))


    def display(self):
        for idx, account_info in self.account_infos.items():
            print(f"{idx}: {account_info['account']}")

    def getAccount(self, idx):
        return self.account_infos[int(idx)]

