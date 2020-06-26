# bilibili-danmaku-regex
结合[pakku.js](https://github.com/xmcp/pakku.js)使用的自用B站弹幕屏蔽正则

## 怎么用
### 1. 使用pakku黑名单（推荐）

1. 全选并复制[Raw文件](https://raw.githubusercontent.com/Mark9804/bilibili-danmaku-regex/master/B%E7%AB%99%E5%BC%B9%E5%B9%95%E5%B1%8F%E8%94%BD%E6%AD%A3%E5%88%99.txt)
2. 粘贴到到Pakku黑名单中（黑名单功能需要开启全部设置方可见）![示例](https://github.com/Mark9804/bilibili-danmaku-regex/raw/master/images/pakku-blacklist.png)
3. 保存（已打开的视频需要刷新之后才能正确应用黑名单）

⚠️**注意：Firefox版pakku不支持前后向查找**，请尽可能使用Chrome。如果一定要使用Firefox的话需要删除包含前后向查找的正则（以`(?!`或`(<!`为开头）

### 2. 使用B站自带过滤器

1. 下载或自行复制保存[XML文件](https://raw.githubusercontent.com/Mark9804/bilibili-danmaku-regex/master/B%E7%AB%99%E5%BC%B9%E5%B9%95%E5%B1%8F%E8%94%BD%E6%AD%A3%E5%88%99.xml)
2. 在B站播放器“屏蔽设定”的空白位置**右键单击**，选择“导入XML文件”![示例](https://github.com/Mark9804/bilibili-danmaku-regex/raw/master/images/bilibili-blacklist.png)
3. 应用相关设置

⚠️XML文件是自动生成的，我没有测试过。如果出现应用文件后弹幕全部消失的情况请清除屏蔽列表中正则表达式内容；如果导入失败请删除包含前后向查找的正则（以`(?!`或`(<!`为开头）

另外推荐一个网站：[Bilibili 屏蔽词分享平台](https://harrynull.tech/bilibili/#sharelist) 本正则已集成其中大部分个人认为需要的规则。但是**网友的创造力是无穷的，遇到漏网弹幕也希望大家能够提出PR和[Issue](https://github.com/Mark9804/bilibili-danmaku-regex/issues)，共建美好B站**。
