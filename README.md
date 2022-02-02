# playwright-dojo 概要

Playwright 道場

作成日 2022/02/02

## 01. ファイル・フォルダ構成

```text
--playwright-dojo/
  |--apps/    ... 自作モジュールの置き場
  |--logs/    ... ログファイルの置き場（※1）
  |--temp/    ... 一時ファイルの置き場（※1）
  |--tests/   ... テストスクリプトの置き場
  |--.env     ... 環境変数に組み込むキーバリュー（※1）
  `--main.py  ... ブラウザ自動化 実行スクリプト

※1 ... リポジトリから除外
```

## 02. Python 環境の構築

- OS は WSL2 上の Ubuntu 20.04 を想定
- エディタは Visual Studio Code を想定

```bash
cd ~/playwright-dojo
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt -c constraints.txt
```

### .vscode/settings.json 設定例

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Path": "venv/bin/flake8",
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "autopep8",
  "python.formatting.autopep8Path": "venv/bin/autopep8",
  "editor.formatOnSave": true,
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "/home/{{YOURNAME}}/playwright-dojo"
  }
}
```

※ `{{YOURNAME}}`は適宜変更する

### Playwright 用ブラウザのインストール

```bash
cd ~/playwright-dojo
source venv/bin/activate

# playwright コマンドが使えることを確認する
playwright --version
# => Version 1.18.2

# Chromiumをインストールする
playwright install chromium
```

インストールされたブラウザのありか

```text
~/.cache/
  `--ms-playwright/
      `--chromium-956323/
          `--chrome-linux/
              `--chrome
```

## 03. 実行スクリプトの使い方

```bash
cd ~/playwright-dojo
source venv/bin/activate

# ブラウザ自動化スクリプト
python main.py first
python main.py job1 --suffix=01
python main.py job2 --suffix=01
```
