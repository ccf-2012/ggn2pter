
# ggn2pter修改版

在原代码基础上，加以下修改：
1. 添加下载器的支持（当前仅支持qb)， 体现在：
   1. 在首次配置时将提示设置host, port, username, password
   2. 在输入ggn 下载link后，将此链接推送到下载器中开始下载
2. 写了一个 `seedpter.py` 用于将生成的 `[PTer]` 种子推送到下载器

## 使用方法：
1. 依照下述原说明运行：
```sh
python main.py
```
  首次运行，依照提示填写:
  1. 猫站cookie : 在猫站网页上按F12到网络-请求标头中找cookie拷贝过来
  2. 猫站passkey : 在猫站个人控制面板中找来拷贝过来
  3. 是否匿名发布 : 填 no 吧
  4. 种子下载路径 : 在运行脚本的机器上，找到一个位置，用于存储下载的种子，将会分出三个子目录：`ggn`，`pter`, `backup`
  5. 是否为GGn elite gamer 及以上 : 字面意思
  6. ggn的apikey : 在ggn页面上个人id边上的 `Edit` 点进去，拉到后面找Api Key字样，建一个api，记下字串（找个地方保存), 拷贝过来
  7. QB的host : （新加的）用于下载和作种的qBittorrent，只填IP
  8. QB的port : （新加的）用于下载和作种的qBittorrent, Port
  9. QB的username : （新加的）用于下载和作种的qBittorrent, 用户名
  10. QB的password : （新加的）用于下载和作种的qBittorrent, 密码
  将生成 `config.ini`, `cookies.json` 和一个空的 `ggn_links.txt`


2. 再次运行 `python main.py`, 依据提示输入：
   1. GGn种子下载连接
   2. 然后会问几个关于游戏的问题
   3. 将会在猫站发布游戏，并生成可用于猫站发布的种子，存在前述种子下载路径的 `pter` 子目录中，然后提示结束

3. 查看qb中ggn的种子是否已经下载完成，完成后，运行：
```sh
python seedpter.py
```
将会将刚才生成的猫站种子（位于前述种子下载路径的 `pter` 子目录中)，上传至所设置的qb下载器中，开始作种。
上传后的种子，将被移到种子下载路径的 `backup` 子目录，保持`pter` 子目录为空
> qb有种子完成后运行一个命令的功能，可以调用此功能进行自动上传种子作种


以下为原说明
-------

# ggn2pter GGn快捷转种工具![python](https://img.shields.io/badge/python-3.7-blue)![time](https://img.shields.io/github/last-commit/scatking/ggn2pter)<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)<!-- ALL-CONTRIBUTORS-BADGE:END -->


## 简介

该脚本能够在你输入GGn的下载链接后自动获取相关信息并下载种子，同时自动将种子上传至PTerClub

---
## 工具特点
* 自动转种并能够下载相关种子，方便配合BT客户端实现自动做种
* 支持有 `steam` `epic`或`indenova`条目的游戏
* 支持位列于 [platforms.txt](platforms.txt)目录下的平台
* 支持转载 `游戏本体` `更新补丁` `修改器` `DLC` `GAMEDOX`

## 依赖环境 

###  python模式

* Python 3
*  Mac, Linux, Windows

### 可执行文件模式

* Windows, Linux

## 安装指南

### Python 模式

#### 1.克隆我的仓库
~~~~shell
git clone https://github.com/scatking/ggn2pter.git
~~~~
当然你也可以直接下载源码包后解压使用：
~~~~
https://github.com/scatking/ggn2pter/archive/master.zip
~~~~
#### 2.安装相关依赖
~~~~shell
pip install -r requirements.txt
~~~~
如果你无法安装的话可能是你的用户权限不够，尝试使用`sudo`安装；对于某些同时装有`python2` 与 `python3` 的用户，可能需要指明`pip`的版本，如 `pip3`
~~~~shell
sudo -H pip install -r requirements.txt
~~~~
#### 3.运行使用
~~~~shell
python main.py
~~~~
### 可执行文件模式

#### 稳定发布版

##### 1. 下载发布文件

前往 [发布页面](https://github.com/scatking/ggn2pter/releases ) 下载最新的发布文件

##### 2. 解压后双击`ggn2pter.py`运行使用

#### 最新版

#### 1. 下载发布文件
前往[Github Action](https://github.com/scatking/ggn2pter/actions)对应平台下载最新构建的发布包

##### 2. 解压后运行使用

## 使用指南

### 1.填写配置信息
第一次运行时，程序会让你填写一些配置信息，按照实际情况填写即可：
* 猫站`passkey`
* 匿名选项
* 种子下载目录
* 是否为`elite gamer`
* 站点`cookies`（见下文）
* GGn的Api Key （见下文）

### 2.1 填写cookies
第一次运行程序时，程序会让你输入GGn与猫站的cookies，按照提示输入即可：
![cookies.png](https://img.pterclub.com/images/2021/03/15/2021-03-15-223914.png)
如果不知道如何获取cookies的，可以参考[常见问题](https://github.com/scatking/ggn2pter#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)

### 2.2 填写GGn API key
GGn目前已经支持Api请求模式，由于该模式不需要再访问网站，因此该模式更加快捷简便，同时也更加安全，强烈建议填写API Key启动该模式。
* 前往GGn `edit`页面，下拉找到` API Keys `栏目，输入名称并勾选`Torrents`栏目：
![API](https://i.vgy.me/T0rZxV.png)
* 点击最下方保存栏目后页面上方会弹出API Key，注意保存
![KEY](https://i.vgy.me/GzLeuP.png)


### 3.选择运行模式

#### 3.1 单种模式
直接输入GGn的下载链接即可，工具会尝试上传该种子

#### 3.2 批量模式
1. 事先编辑ggn_links.txt文件，将下载链接每行一个输入进文本
2. 直接回车不输入任何命令，工具将读取链接并尝试上传链接里所有游戏；在上传完毕一个种子后，会将该链接从文件中删除。

### 4.等待程序运行

### 5.选择游戏信息
如果程序认为将要上传的种子的游戏信息可能已经存在于猫站，会返回一个列表让你选择游戏信息，如果不存在相关游戏的话，系统会自动上传到猫站。
```shell
我们在猫站找到以下游戏，请选择要上传的游戏分组（输入编号(并非gid)即可，如果没有请输入0）：
1.Windows: Cooking Simulator GID:3409
编号： <输入编号>
```
### 6. 选择indienova条目（仅主机）
对于没有`steam`和`epic`条目的主机游戏，脚本会自动搜索indienova网站并返回一个游戏列表，此时需要输入列表中的编号
```shell
未找到steam或epic链接，正在前往indenova查询
... ... ...
1.Cooking Simulator (2018)|g※|厨房模拟器|g※|
2.Cooking Simulator: Cakes and Cookies (2020)|g※|厨房模拟器：蛋糕和曲奇饼|g※|
请输入适配游戏的序号：<输入编号>
```
### 7.输入种子额外信息
由于无法从GGn稳定获取游戏地区，中文字幕与国语配音的相关信息，需要用户手动输入：
![moreinfo.png](https://img.pterclub.com/images/2021/03/15/2021-03-15-224809.png)

### 8.审查种子标题
脚本会自动将GGn的标题转换为符合猫站规则的标题，但是仍然需要用户进行检查。如果有错误请输入正确的标题，无误则直接回车。
~~~
智能检测到的种子标题为-TiNYiSO，若有错误，请输入正确的标题，没有请直接回车：
~~~

### 8.上传完成

## TO DO LIST
* [x] 批量模式
* [ ] verified dump
## 常见问题
* Q. cookies 是个什么东西呀?怎么获取呀？
* A. cookie 是来存储你登陆信息的一串字符，下面我以firefox为例演示一下怎么获取。
* * 按下F12进入开发者工具，并切换至`NETWORK/网络`栏目：
* * ![Network.png](https://img.pterclub.com/images/2021/03/22/10ac0ff23048ed11c.png)
* * 单击你左上角的用户名，载入你的用户界面
* * 找到`NEWWORK/网络`栏目里加载出来的user.php之类文件，并单击它：
* * ![user.php.png](https://img.pterclub.com/images/2021/03/23/2.png)
* * 找到`request header/请求头` 中cookie项目中的字段并复制下来：
* * ![cookies.png](https://img.pterclub.com/images/2021/03/22/3abed1483ad76c9a6.png)

## 贡献者 ✨

感谢以下诸位的共同协作:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/tlwzzy"><img src="https://avatars.githubusercontent.com/u/36352458?v=4?s=100" width="100px;" alt=""/><br /><sub><b>tlwzzy</b></sub></a><br /><a href="https://github.com/scatking/ggn2pter/commits?author=tlwzzy" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
