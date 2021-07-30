# Mabinogi-auto-login

其實就是省去輸入帳密的時間而已，還是透過beanfun網頁登入, 而且還是有些許手動部分XDD

## 使用說明
### 選項一、直接下載[最新版本執行檔](https://github.com/andyChuang/Mabinogi-auto-login/releases)
1. 下載Mabinogi-auto-login-via-web.zip並解壓縮
2. 在同Mabinogi-auto-login-via-web資料夾內建立`account.json`，格式如下：
```
[
{
"account": "帳號1",
"password": "密碼1",
"game_account": "遊戲帳號1"
},
{
"account": "帳號2",
"password": "密碼2",
"game_account": "遊戲帳號2"
},
.
.
.
{
"account": "帳號N",
"password": "密碼N",
"game_account": "遊戲帳號N"
}
]
```

3. 執行Mabinogi-auto-login-via-web.exe，並依指示選擇你要登入的帳號
4. 程式會自動執行直到跳出下列畫面，接下來請手動進行
![螢幕擷取畫面 2021-07-31 003542](https://user-images.githubusercontent.com/2863011/127684391-986493d6-ece4-42c1-926b-df633b37018e.png)
6. 遊戲畫面跳出後就可以把程式和網頁關掉了

### 選項二、如果你擔心我會偷你的帳密，你可以直接下載原始碼，檢查過後再用
1. 首先你要有裝python3 (建議3.7)
1. Clone this repository to wherever you want
1. `cd Mabinogi-auto-login`
1. `pip install -r requirement.txt`
1. 同目錄下建立`account.json`，格式如下：
```
[
{
"account": "帳號1",
"password": "密碼1",
"game_account": "遊戲帳號1"
},
{
"account": "帳號2",
"password": "密碼2",
"game_account": "遊戲帳號2"
},
.
.
.
{
"account": "帳號N",
"password": "密碼N",
"game_account": "遊戲帳號N"
}
]
```
6. python play.py
7. 程式會自動執行直到跳出下列畫面，接下來請手動進行
![螢幕擷取畫面 2021-07-31 003542](https://user-images.githubusercontent.com/2863011/127684391-986493d6-ece4-42c1-926b-df633b37018e.png)
8. 遊戲畫面跳出後就可以把程式和網頁關掉了

## To-do

## Change Log



