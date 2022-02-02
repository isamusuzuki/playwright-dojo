import json
import shutil
from logging import INFO
from os import mkdir, path
from time import sleep

from apps.browser_auto.apple import apple
from apps.browser_auto.bacon import bacon
from apps.browser_auto.cacao import cacao
from apps.util.logger_a import getLoggerA

from dotenv import load_dotenv

from fire import Fire


class Main():
    def __init__(self) -> None:
        self.logger = getLoggerA(__name__, INFO, 'console')

    def first(self) -> None:
        """
        ブラウザを自動実行する
        """
        apple(logger=self.logger)

    def job1(self, suffix: str) -> None:
        """
        楽天市場の商品ページから商品画像のURLを取得する

        あらかじめ temp/itemcodes{suffix}.jsonを用意しておくこと
        ["ahc3601", "oajon3"]

        Parameters
        ----------
        suffix: str
            ファイル名に使っている接尾辞
        """
        json_file = f'temp/itemcodes{suffix}.json'
        with open(json_file, mode='r', encoding='utf-8') as f:
            itemcodes = json.loads(f.read())
        result_dict = {}
        for item_code in itemcodes:
            self.logger.info(f'item_code = {item_code}')
            result_dict[item_code] = bacon(
                item_code=item_code, logger=self.logger
            )
        json_file = f'temp/itemimages{suffix}.json'
        with open(json_file, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(result_dict, ensure_ascii=False, indent=2))
        self.logger.info(f'done => {json_file}')

    def job2(self, suffix: str) -> None:
        """
        Yahoo!ショッピングの商品ページからiFrame内のHTMLを抜き出す

        あらかじめ temp/itemcodes{suffix}.jsonを用意しておくこと
        ["ahc3601", "oajon3"]

        Parameters
        ----------
        suffix: str
            ファイル名に使っている接尾辞
        """
        # ターゲットフォルダを空にする
        target_folder = f'temp/html{suffix}'
        if path.exists(target_folder):
            shutil.rmtree(target_folder)
        mkdir(target_folder)

        json_file = f'temp/itemcodes{suffix}.json'
        with open(json_file, mode='r', encoding='utf-8') as f:
            item_code_list = json.loads(f.read())
        for item_code in item_code_list:
            self.logger.info(f'item_code = {item_code}')
            cacao(
                item_code=item_code,
                target_folder=target_folder, logger=self.logger)
            # しばし待つ
            sleep(2)


if __name__ == '__main__':
    load_dotenv()
    Fire(Main)
