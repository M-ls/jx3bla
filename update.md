#更新日志

(TODO)增加BOSS战斗结束后不弹出复盘的功能，包括手动关闭，以及过短的记录不弹出。

(TODO)修复上传的数据接锅太多时，会导致程序卡住的问题。

(TODO)1.2.4 个位数级别属性对齐

(TODO)4.1.12 图片转存

(TODO)5.11.1 移除XiangZhi和Actor中无意义的类成员变量，特别是可以从config中获取的部分

# (TODO)7.5.0

(TODO)灵素复盘

# 7.4.0

## 功能

为奶歌复盘@雷域大泽加入评分系统。

奶歌复盘展示界面支持网页版，现在可以通过网页查看联机保存的复盘结果。

新增6号的复盘，包括P1/P2承伤，触手承伤，蛾卵承伤，P3承伤及存活时间。

新增2号的复盘，包括BOSS/锁链/蜘蛛卵承伤。

在奶歌复盘中显示统计并显示覆盖率的热力图。

在奶歌复盘中支持APS的推测。

在奶歌复盘中统计枕流的HPS。

增加对国际服繁体字的支持，包括文件名和简单的BOSS名。

## 修复

修复3号、5号的剧情脱战时间，现在在进入通关剧情时立刻算作脱战。

修复一个可能导致奶歌的宫技能不连续的问题。

修复本地查看指定编号时常失败的问题。

修复有时部分阵眼的主动技能会将统计中连续的技能中断的问题。

# 7.3.0

# 功能

新增4号的复盘，主要统计对不同目标的伤害，时间轴，控制，脱战时间。

在装分显示中为大橙武添加一个发光特效，排面！

在战斗回放中显示橙武特效和特效腰坠。

在奶歌复盘中显示玉简DPS统计。

细化5号的统计，现在将锁链DPS统计区分奇数与偶数（通常是偶数锁链缺承伤，容易出事）。

对5号的曲云蝶鸾统计进行区分，区分驱散焦土与驱散天锁。

增加5号的打断统计。

将5号被点天锁记为被控时间。

## 修复

装备统计更新择芳套装（早该更新的，是我把这事忘了= =）

修复3号的统计有时会卡住导致复盘失败的问题。

修复复盘模式手动选择时，如果遇到太长的文件名，会卡掉多选框的问题。

修复在某些情况下统计不到进战数据，导致覆盖率爆炸的问题。

# 7.2.0

## 功能

增加BOSS名称回流功能。即使文件名中的BOSS不准确，也可以通过战斗记录尝试复原BOSS。

增加月泉淮拼接功能，现在在复盘模式、实时模式下读取到连续的不完整月泉淮记录时，会尝试进行拼接。

实现月泉淮的详细复盘，包括中火统计，各种DPS，时间轴。

## 修复

修复白帝1号承伤失败时有时会卡住的问题。

修复jcl文件丢失战斗时间信息时，会复盘失败的问题。

修复万剑归宗、蟾啸等打断判断不一定准确的问题。

修复奶歌不器会使技能回放中断的问题。

# 7.1.2

## 界面

优化3号打断复盘的格式，增加可读性。

复盘模式选文件从30个增加到50个，以处理一些极端情况。

## 修复

修复1号拉脱会导致复盘失败的问题。

# 7.1.1

## 修复

修复3号的打断复盘对yx以外的数据无效的问题.

修复3号的击杀判定有时不准的问题，现在绑定到通关喊话上.

# 7.1.0

## 功能

加入3号的详细复盘，统计小怪DPS、打断复盘、时间轴等记录。

在奶歌复盘中，对梅花三弄、HOT的覆盖率统计中，排除重伤时的部分.

在奶歌复盘中增加战斗人数统计，记录全程平均人数.（主要是考虑老板数量）

更新装备打造统计，统计五彩石、附魔的情况.

在奶歌复盘中增加装备打造显示.

更新属性计算方法（7、8级镶嵌），更新装备列表以计算新的装备（热更新）.

在演员复盘的重伤记录中，支持jcl数据显示技能与buff名称.

## 界面

更新药宗的门派染色显示.

更新奶歌复盘中技改之后的奇穴名称。

为灵素复盘提供接口.

复盘模式选文件的界面调整为左对齐，并倒序显示.

在战斗统计中将治疗颜色从绿色调整为深绿色，避免瞎眼.

## 修复

修复有时攻防的喊话会混到正常统计中，使jcl复盘格式不正确导致统计卡住的问题.

修复服务器中公开与未公开被反转的问题.(热修复)

# 7.0.10

## 修复

修复实时模式下分锅界面不正常的问题。

修复提前开怪统计可能不正常的问题。

修复没有通关但是数据可能仍被上传的问题。

移除实时模式下的几个屏幕输出。

# 7.0.9

## 修复

修复文件格式保存错误导致主界面打不开的问题。

修复复盘数据过长时可能会导致保存失败的问题。（热修复）

修复服务器崩溃时未能正确返回崩溃信息导致复盘也卡住的问题。（热修复）

# 7.0.8

## 功能

删除大部分调试代码。

维护gitignore，整理代码结构。

(TODO)更新发布流程，添加一个从解包表读取装备信息的流程。

维护新的文档，视频，以及各种攻略的文案。

## 修复

修复25pt模式宫傲水下阶段计算时间可能错误的问题。（这还有必要修吗……）

修复jx3dat模式下文件名切分错误的问题。

尝试在服务器数据库保存失败的情况下依然返回复盘结果。

# 7.0.7

## 功能

补全白帝5,7号的复盘，至此白帝1-7号的复盘全部更新完毕。

补全雷域大泽1-6号的脱战判定，至此1-6号的全部数据均可上传。

在服务器端补齐雷域大泽的战斗记录显示页面。

在设置界面新增一个指定编号读取上传的数据的功能。

在奶歌复盘pro中增加装备导出功能。

在奶歌复盘pro中增加web版链接，并给出访问方式。

在设置文件中加入版本信息，方便在版本更新时进行某些操作。

实现装备强化信息统计功能。

自动打包与展开图标包。

加入风雷的统计。

## 修复

选文件的界面设置上限为30条，避免条目太多把窗口卡住。

修复白帝1号承伤失败时会把界面卡住的问题。

修复徵的统计，现在会统计古道，同时盾的统计增加平吟和犹香。

修复精炼、镶嵌、五行石五彩石、套装等出错时会把配装器卡住的问题。

修复经验值不显示的问题。

修复名称打码的位置，避免在数据中的打码污染流程。

修复1号的寒光旋被重复统计的问题。

修复路径中如果含有部分符号，会使BOSS名称解析错误的问题。

# 7.0.6

中间测试版本，包含7.0.7的部分更新。

# 7.0.5

## 功能

补全白帝1-4,6号的专属复盘。

修复白帝江关2号的进战时间为赵八嫂本体进战时间。

添加药宗的识别与支持。

添加新本及BOSS的识别，并且添加每个BOSS的框架，尝试判定其是否挑战成功。

尝试正确计算jcl下召唤物的DPS与HPS。

尝试对齐jcl和jx3dat的战斗时长。

在奶歌复盘回放中增加一指回鸾。

复盘模式结束时自动弹出总结界面。

## 修复

修复已经复盘过的数据使用新版本的警长复盘时，会导致数据库插入失败的问题。

修复基准路径不为当前路径时，会使BOSS名称识别失败的问题。

修复基准路径不为当前路径时，会无法使用复盘模式扩展功能的问题。

调整了复盘模式扩展的界面，使其可以正常滚动。

修复同一战斗记录中有多个奶歌时，会使部分统计数据不准确的问题。

修复部分情况下普通徵不统计的问题。

删除演员复盘设置中的废弃选项。

修复隐藏技能被统计导致连续的技能中断的问题。

修复测试服如果装备了新的大附魔，会把整个流程卡住的问题。现在用一种通用的方法来为未识别的装备保底。

修复地图名称变动导致演员复盘数据上传失败的问题。

修复有时技能延迟是负数的情况。（这里的负数延迟主要是加速获取失败导致的，现在强行忽略负数）

修复徵的数量经常显示不正确的问题。

# 7.0.4

## 功能

为复盘模式增加文件选取的功能。现在除了自动选取外，也可以手动选取需要复盘的文件。

为实时模式增加一个关闭功能。

更新部分不复杂的白帝江关BOSS（2，4）的专属复盘。

尝试在宫威计算BOSS技能轴，并且显示在战斗回放中。

## 修复

修复了jcl格式下缺名字的问题，这通常是因为第一次获取名字失败，例如赵八嫂。

尝试修复数据库有时会卡死的问题，需要进一步定位。

修复战斗回放中同一技能间隔过长时仍被连在一起的问题。

恢复自动更新功能。

#7.0.3

## 功能

调整了复盘模式与实时模式的设置，现在可以正确地开启两种模式了。

将战斗复盘界面调整为优先出现，分锅界面及门派复盘界面在其中作为子界面。

完善加速设置，现在可以在设置中指定加速以处理自动解析失败的情况，或是强制指定加速。

支持在设置中指定是否计算T心法的覆盖率。

## 修复

修复更新版本的数据无法正常上传到服务器的问题。

#7.0.2

## 功能

支持奶歌复盘pro的自动上传。

## 修复

修改战斗效率算法，修正战斗效率没有计算连续技能中的空白的问题。

修复jx3dat下服务器信息多一个引号的问题。

#7.0.1

## 功能

更新了奶歌复盘pro的本地GUI，现在支持所有的显示了，但是需要图标包才能正常使用。

#7.0.0

##功能

实现属性自动计算，现在可以通过服务器的/getAttribute来计算奶歌属性（开发者功能）。

支持读取jcl，并且在设置中提供选项，指定jcl与jx3dat模式二选一。修复jx3dat文件夹格式的问题。

关闭奶歌复盘入口，实现奶歌复盘pro的初步形式，相比原本的奶歌复盘支持技能统计与战斗回放。复盘结果以文字形式打印在终端。

#6.11.0

##功能

加入4号的详细复盘。

由于DPS天梯已关闭，因此不再尝试上传DPS天梯。

##优化

蛊惑传递的治疗量，小于2000时将不再显示。

##修复

修复7号过快拉脱会导致复盘失败的问题。

修复1号承伤人数达到5人时仍然判定承伤失败的问题。

修复部分过期五行石会导致程序崩溃的问题。

#6.10.2

##修复

修复部分带老七的数据无法生成奶歌复盘的问题。

#6.10.1

##修复

修复提前开怪判定无法显示的问题。

修复部分情况下奶歌复盘无法生成的问题。

#6.10.0

##功能

加入5号的详细复盘。

加入5号的传染判定，并且yx不再判定下阶段之后的传染。

##修复

修复奶歌复盘在大部分情况下会卡住，导致无法生成图片的问题。

#6.9.0

##功能

加入1号的详细复盘。

重伤复盘中加入可能的断禅语监控。

重伤复盘中加入易伤、减疗层数。

重伤复盘中加入对应的技能是否会心。

重伤复盘中加入蛊惑众生的判断。

在3号复盘中，加入眼中钉复盘（被推的人>=5时，视为中眼中钉buff的人接锅）

##优化

在3号复盘中，锁链复盘相关内容只有英雄难度才会出现。

将藏剑门派的染色略微调深。

英雄难度下，宫傲的水球砸人不再记录人数<3的承伤。

##修复

修复宫傲的水球在25pt以外的难度数值不准确，导致水球承伤计算有时会出错的问题。

修复上传的数据接锅太多时，会导致程序卡住的问题。

#6.8.1

#修复

修复杯水在未到时间时因为未知原因重伤，也会被判定为杯水的问题。

修复锁链复盘有时会导致程序崩溃的问题，同时修复有时会将最后一次QTE判定为超时的问题。

修复QTE按错由于拥有诡异的判定，导致无法正常识别的问题。

修复达摩洞老四的闪腿害人名单会重复的问题。

#6.8.0

##功能

加入3号海荼的详细复盘，包括各阶段DPS，与转阶段后的锁链监控。

##修复

修复了部分情况下重伤记录不足20条的问题。

修复了反弹伤害不会计入重伤记录的问题。

修正了邪水之握的统计，现在可以统计到因为血圈被抓到的人了。

#6.7.1

##修复

修复yx白帝不会自动上传DPS天梯的问题。

修复了7号乱流复盘中，会错误地清除水球产生时间导致复盘崩溃的问题。

修复了3号通关喊话不正确的问题（应该是正式服修改了）。

修复了天网系统的历史犯错记录中时间错乱的问题。

#6.7.0

##功能

增加白帝江关1-7的通关判定。

对白帝江关统计数据进行优化，尝试统计装分并预留详细分析的空间。

增加白帝江关1-7的详细复盘页面框架，使其可以上传数据。

增加装分解析与特殊装备概览。

增加7号的额外邪水之握分锅、转球分锅。

添加7号的详细复盘页面（简易版本），记录水球承伤。

增加3号的下水分锅逻辑，在后续版本3号详细分锅功能实现后实装。

##优化

针对6.7.0补全文档。

7号的个人被水球击中调整为非严重犯错。

7号被邪水之握直接重伤调整为非严重犯错。

重伤记录中，历史记录调整为20个。

增加白帝江关的天网DPS统计。

#6.6.0

##功能

增加点赞、吐槽功能。

增加荣誉值与积分系统，并增加升级逻辑。上传数据时，可以获得对应的积分与荣誉值。

增加点赞与吐槽能量兑换券，以及在数据库中增加对应的字段。

天网系统增加信誉分，并且可以显示与排序。

在天网系统中加入白帝江关相关的选项。

为积分系统添加文字说明。

加入配装导出到剪贴板的功能。

重伤记录加入颜色区分。

##优化

对上传的数据增加用户ID、时间等补充。

在上传的数据中增加版本转换字段。

将天网系统的一部分运算移动到后端，并简化前端的逻辑。

##修复

修复了在复盘模式下，选中上传DPS天梯但不会上传的问题。

#6.5.0

##功能

加入配装导出功能（暂时只支持花间）。在*公告*中可以进一步看到使用方法。

在复盘数据不完整时，跳过崩溃逻辑（改为弹窗提示），以支持配装导出功能。

#6.4.1

##修复

修复奶歌复盘在白帝江关无法运行的问题。

#6.4.0

##功能

增加客户端唯一识别码，为之后的互动功能或个性化设置提供基础。

在重伤复盘中增加治疗的记录，方便对重伤原因做出更准确的判断。

在全程战斗中发生过人物替换时，保证结果界面依然可以正常显示。

支持体服白帝江关的BOSS名称。

在10人难度中增加体服7号的点名查锅。

##界面

在*设置*界面中新增一个*用户*窗口，用来记录当前用户的状态。

在*用户*窗口中增加一个*用户名*，可以填写自己的ID用于社区交流。

在复盘界面，当详细复盘不支持当前BOSS时不再显示*未知*，而是显示战斗记录中的BOSS名。

##优化

4号的踢球，6号的玩剑作为补贴项写入分锅记录中。

#6.3.0

##功能

在有效DPS界面中，对治疗职业也显示HPS，并显示在团队-心法DPS一栏。

在1-6的详细查锅中，实装团队-心法DPS。

增加手动分锅功能，可以在分锅界面手动输入描述来添加新的锅。

增加6号磁力引爆查锅，包括早解与爆炸。

对设置文件多进行一项检查，保证最大历史记录为50以上，战斗记录最短时间10秒以内。此功能可以在设置中跳过。

##优化

在详细复盘中，治疗量相关的数值将显示为绿色。

为6号的传功顺序添加一个颜色渐变的功能。

天网页面的服务器增加下拉菜单。（热更新）

DPS统计重做，使用新的数据计算心法DPS平均数。

修改天网系统黑历史的显示逻辑，增加“犯错率”进行记录。（热更新）

##修复

修复6号的被控时间被乘了传功次数的问题。

修改了天网页面及奶歌天梯页面，使其支持更多的浏览器版本。（热更新）

修复部分上传的DPS数据为非整数的问题。

修复了在某些DPS为0的情况下会导致复盘崩溃的问题。

当复盘过程中出现bug时，尝试直接跳过当前复盘，从而不卡住主界面。

#6.2.0

##功能

更新6号首领的详细查锅，至此达摩洞1-6的详细查锅已经全部更新完毕！

天网系统加入指定查询功能，可以查询某个区服指定的某些玩家的记录。

增加*复盘*按钮。现在即使关掉了复盘界面，也可以点击此按钮来打开最后一次记录了。

移除复盘模式下的演员复盘图片。现在在复盘模式下也会以原本实时模式的方式来解析，通过*复盘*即可查看。

将*分锅结果*界面调整为*总结*。在其中可以像之前一样看到每个人的锅数。在之后的版本中，可以通过这一页面直接出警。

在*总结*页面中显示所有的战斗记录名称。可以通过点击按钮来快速切换到对应的战斗复盘。

##优化

在实时复盘崩溃时，加入一个异常处理，保证在一个复盘崩溃后可以复盘其它的记录。

1号的引导玩家不再记录狂热崇拜层数叠加。

2号的引导玩家不再记录魅惑。

3号的鬼门针重伤、4号的横绝气劲·爆重伤、4号的堕天腿重伤、5号的嗔重伤记为灰色。

6号的狂雁与落鹰，如果通过推测的方式得到，则会一次性标记2层或3层。

在6号的战斗结束时，会提醒玩家点击复盘模式，来复盘奶歌的记录。

6号的传功层数，现在8层以下会被标记为严重犯错，只有9层才是灰色。

在实时模式完成后点击复盘模式，将读取缓存而不是重新读取文件，从而加速运行效率。

在实时模式完成后，若BOSS未通过，则会清理这条记录对应的内存。

##修复

修复关键治疗量有时会吞掉结束状态，导致数值不准的问题。

修复2号引导驱散的时间不显示的问题。

修复4号的详细复盘偶尔会卡住的问题。

修复奶歌复盘中，血歌偶尔会被判断成莫问的问题。

#6.1.0

##功能

更新5号首领的详细查锅。

为实时复盘加入一个复制功能，方便在团队中出警。

为天网系统添加犯错记录，可以简单地看到之前警长统计到的犯过的错。

增加4号闪腿害人的查锅。

##优化

修复在提前开怪统计中，毒经会莫名其妙背锅的问题。

实时模式设置成功时，不会再出现红色的提示了。

在天网系统中，移除同一份战斗记录由不同版本号导致的不同数据。

修改唯一值算法，在后续提交的数据中同时考虑团队成员、时间，并根据版本号进行更新。

在奶歌复盘中增加析构，防止多次点击复盘模式导致记录重叠。

yx5号及全难度6号不再显示DPS参考线。

#6.0.1

##优化

修复4号在非英雄难度下通关判断错误的问题。

修复上传的数据中，面板治疗界面打码失败的问题。（但是只对之后上传的数据有效……啊这个祖传打码）

修复25普通达摩洞的奶歌复盘会失败的问题。

#6.0.0

##功能

更新4号首领的详细查锅。

在2号首领的详细查锅中，增加引导的具体时间，与小怪灭团喊话的时间。

为6号的层数复盘增加死亡时推测的功能。

加入英雄达摩洞的奶歌评分。在这个标准中，难度会比普通更大一些。

增加奶歌复盘天梯，支持通过网页浏览已经上传的数据。

增加天网系统，支持通过网页批量查询对应服务器玩家的历史最高DPS，后续还会增加犯错记录等。

支持超短记录的战斗复盘，可以在游戏中取消时间限制，从而快速得到团队信息，与天网系统联动。

##界面

在复盘文件格式出错时，增加正确的提示。

优化主界面中的提示栏，并增加一行文字显示区域。

在实时模式中增加显示进度的功能。

在公告中添加帮助界面，指引下载文档、加入反馈群、与复盘指引。

在公告中添加更新界面，可以看到本更新内容列表。

##优化

为快速模式增加一个警告框。

自动获取路径时，在有多个符合条件的角色名时，选取距离修改时间最近的一个，防止选到过期角色。

在设置界面，如果点击了角色或是剑三路径，就会自动清空基准目录，防止表现与预期不一致。

增加生成图标功能，彻底解决win10通知的空报错。

在用户协议未同意时尝试锁住界面。

在奶歌复盘中排除老五的机甲与老六的爆杀。

修复前后切换实时复盘记录时，详细统计会显示不出来的问题。

修复老四在记录者意外死亡之后，刷新的不完整数据被记录为通关数据的问题。

#5.9.0

更新6号的层数检查。现在会尽可能推理出在战斗过程中给boss叠层数的位置，并计入分锅记录。

在上传到DPS天梯榜后，在窗口中显示对应的链接。

为可能的版本号溢出提供特别判定。但由于之前的版本没有更新此功能，下一个版本号依然会升级到6。

#5.8.2

修复2号宓桃在部分情况下会把非玩家目标计入DPS，而导致复盘崩溃的问题。

修复2号宓桃在部分情况下驱散由于复盘记录倒转导致计算错误的问题。

修复奶歌复盘下，2号宓桃在引导阶段团灭，导致无法计算引导阶段时间的问题。

#5.8.1

修复3号首领的复盘，在一些情况下会丢失鬼门针的信息的问题。

#5.8.0

更新3号首领的详细查锅，支持鬼门针、千丝乱、穿脊牵肌等阶段的详细复盘。

为实时复盘中，win10通知导致的空报错，添加了一个提示。

#5.7.0

更新2号首领宓桃的详细查锅，支持引导、驱散、关键治疗、debuff层数的详情。

调整2号首领宓桃在yx下的逻辑，现在不会因为错误的喊话而乱掉了。

修复2号首领宓桃在引导阶段灭团时，奶歌复盘会崩溃的问题。

在演员复盘的设置中加入一个选项，用于控制是否在复盘结束后，自动将数据上传至罪人榜。（此项默认开启）

#5.6.0

更新yx1号首领的详细查锅，支持P1/P2独立的DPS，层数详情，承伤详情。

调整了1号首领的在各种难度下的崇拜值，增加了易怒之人的统计。

调整了小药警察功能，现在只有3个以上的玩家在战斗中补齐四小药时，才会检查所有玩家了。

修复了团队-心法DPS在部分情况下的顺序，现在不会以随机顺序去除排名偏后的玩家了。

重构了部分演员复盘代码，并加入文档。

#5.5.2

修复了部分情况下在复盘结果界面点击切换，会使界面加载失败的问题。

#5.5.1

修复了部分BOSS的复盘记录会被吞掉，导致整个程序卡住的问题。

修复了小药警察把ID填错的问题。

#5.5.0

在实时模式右侧新增了一个快速模式按钮，点击时会强制开启实时模式，并且自动复盘最新的一条记录。

为实时模式添加了向前/向后切换的功能。现在实时分锅界面只会显示一个，但是可以通过切换来找到之前的记录。

修复了在同时打开多个分锅界面并分锅时，记录会错乱的问题（现在不会同时打开多个了）。

#5.4.2

修复了部分情况下AOE阶段治疗的来源为未知目标，导致整个复盘被卡住的问题。

#5.4.1

修复了部分情况下喊话为空导致整个复盘被卡住的问题。

#5.4.0

加入奶歌复盘中的评分。

尝试加入自动更新系统。现在当检测到新版本时，会主动指引更新。

奶歌复盘新增老二小怪阶段和老五下P的治疗量统计，折算为HPS。

加入pt老六的传功查锅。

加入小药警察功能。当团长要求所有团员在进战后吃小药后，会查出小药不对的玩家并加入分锅记录。

修复了奶歌没有洗桑柔时，奶歌复盘会崩溃的问题。

更新yx老五的名称，现在可以正确识别了。

#5.3.3

修复分锅结果在有两次以上战斗记录时，有大概率将玩家名字复读一次的问题。

在设置茗伊插件集的设置时判定加速，防止反复点击要很久才反应过来。

#5.3.2

修复非标准剑三目录的问题。现在会指定三级目录(目录下应当有bin)也可以正常识别了。

修复奶歌复盘图的BOSS名称还是不对的问题。

#5.3.1

修复了策T和非策T在部分情况下会搞混的问题，现在用撼如雷(444)和号令三军(15115)区分。

修复了老六由于喊话监控错误导致上传失败的问题。

提前加入25yx的DPS统计上传。

#5.3.0

加入老二引导失败时的检测。

修复老四DPS变为原本的2倍的问题。

增加老四、老五、老六的通关判定，现在可以正确判定所有BOSS是否完成了。

由于可以正确判定通关，实时模式恢复上传功能。

加入新版本检测，现在如果版本不是最新版，会提示更新。

加入公告页面，现在在进入时就会加载，并且显示公告。

#5.2.1

修复了部分情况下程序打不开的问题。

#5.2.0

25普通达摩洞增加DPS及格与补贴统计。

增加并修复老二与老三的通关喊话。

修复奶歌复盘用的是上赛季BOSS的问题，现在改用老二、老五、老六的数据。

修复加速等级显示错误的问题。

修复衍天宗门派染色失败的问题。

#5.1.1

修复某个BOSS没有锅时，会清除已有的分锅记录的问题。

#5.1.0

添加余晖的查锅。

修复10人哑头陀复盘会崩溃的问题。

尝试上传达摩洞拉脱的数据，并且为是否全通提供标识。

加入衍天宗的门派信息。

加入余晖、宓桃的战斗结束判定。

#5.0.0

加速、等效DPS修正为110等级。

在主界面加入一个版本号。

#4.5.0

新建一个图形界面来显示用户协议。

在设置界面加入鼠标悬停提示详细用途。

在设置界面实装“自动获取”按钮。

通过地图ID正确识别达摩洞，并加入常态化的统计中。

添加达摩洞奶歌的数据上传，并降低收集门槛，以获取基准数据。

为老六可能出现的名字提供各种支持。

修复实时模式开启时，在未能成功设置的时候就关掉窗口，会导致程序无法正常结束的问题。

#4.4.1

修复宓桃在出男宠时会导致复盘错误的问题。

#4.4.0

在分锅详情中，在团队-心法DPS记录中显示对应心法的平均DPS及在当前团队的参考DPS。

通过体服T的buff对T进行更精确的区分。

奶歌的空闲比例不再计算影子或其它自动施放的技能。这个早该修了……但是和版本同步吧。

#4.3.0

添加哑头陀的查锅。

重新整理首领名称，避免出现首领名称错乱的问题。

实时模式增加详情界面，可以将鼠标移动到记录上查看。

#4.2.1

修复了界面中修改设置文件时描述不正确的问题。

#4.2.0

实装了设置面板。现在无需手动调整config.ini了。

更新了宓桃的查锅及补贴排查。

加入引导修改“仅在秘境中启用复盘”项，防止复盘失败。

#4.1.1

修复了正式服的奶歌有时不能正确复盘的问题。

#4.1.0

修复了战斗复盘在复盘多个BOSS时会缺数据从而无法运行的问题。

更新了猿飞的踢球查锅，快来看看谁是梅西谁是国足吧！

在图形界面新增了设置面板的可视化，但暂时没有实际功能，只能看着玩。

#4.0.2

修复了文件查找界面调用的函数没有引用的问题。

#4.0.1

修复了主界面调用通知会失败的问题。

#4.0.0

更新了演员复盘的实时模式。现在可以在打本的过程中实时统计演员的情况，并手动分锅。

设计了一个简单的主界面，现在需要手动点击复盘模式才能像原来一样开启复盘。

区分各种双心法门派，为后续统计做准备。

分拆了部分代码到独立的文件中，并添加一些注释。

#3.7.0

更改了DPS统计的逻辑，使用“团队-心法DPS”来衡量DPS是否符合要求。DPS评测只会在25人英雄难度的范阳夜变和敖龙岛开启。

演员统计中犯错记录升级为事件记录，用蓝色来标记进行补贴的事件。

使用具体的技能区分了10个门派的双心法。

修改了奶歌复盘和演员复盘时，部分获取心法的逻辑。

修复了范阳夜变在BOSS数不等于5时有时依然会判定为有效记录的问题。

#3.6.3

修复了迟驻带老板时，奶歌复盘偶尔会崩溃的问题。

#3.6.2

修复了敖龙岛的战斗复盘不能正常生成的问题。

#3.6.1

修复了自动生成的config.ini不正确的问题。

#3.6.0

新增在线浏览奶歌复盘结果的功能，在运行结束后会生成可以分享的链接。

增加公告功能，开始复盘之前会先从服务器读取一条公告。

微调数据格式，使其更方便展示。

奶歌复盘的上传数据中加入一些杂项，方便后台进行处理。

在奶歌复盘的设置中新增了一个公开选项，将选项开启使这次复盘结果被公开，在之后的版本中可以通过网站访问。

更换了名称和图标。

#3.5.0

在图片中添加了奶歌评分排位百分比，现在可以显示自己在同一个副本中的排名了。

在演员复盘中添加了提前开怪查询。

增补了上传数据的内容，以便之后的开发。

增加了敖龙岛1-6的通关判定，以上传敖龙岛的演员复盘数据。

奶歌安小逢添加P1和P2站圈站错的犯错查询。

#3.4.1

删除了一个调试逻辑，现在奶歌复盘只在有评分时才会上传全部数据。

奶歌复盘上传数据时，会正确地根据Mask选项的设定来隐藏自己的ID了。

#3.4.0

增加复盘全部的选项，现在可以自动复盘拉脱的数据了，并且可以整理出所有的犯错记录。

更新范阳夜变奶歌复盘的评分指标，现在获取更高的分数将更为严格了。

增加治疗量统计，并略微调整生成图片的格式。

使用部分常用的治疗技能来识别奶妈，现在不会将T计入治疗统计了。（但依然会记录在特殊统计中）

奶歌盾的DPS增益从13.9%修正为11.7%，评分指标按比例修正。

奶歌复盘中，周贽的统计排除转阶段后的部分。

演员复盘的犯错记录增加分级，分为严重与不严重两项。

为演员复盘新增“减疗20层”，“试炼逃避者”。

更新演员复盘的DPS指标，并且计算平均数时，排除重伤过的玩家与低于及格线的玩家。

演员复盘优化安小逢应援按错的显示。

增加用户协议，并尝试上传奶歌评分与演员复盘数据。

#3.3.0

奶歌复盘的盾覆盖率统计中，对于梅花三弄主动技能，现在在20层以上减疗时不会进行统计了。（会略微影响覆盖率的统计）。

在演员统计中，增加了安小逢查假粉按错的功能。

增加了赤镰乱舞命中次数统计，并且加入安小逢奶歌复盘中。

在演员统计中，重伤记录识别反弹和白某死线。

#3.2.2

修复了安小逢记录中如果有未知NPC的死亡记录会导致程序有概率崩溃的问题。

修复了安小逢记录中把迷乱debuff当成走火入魔，导致入魔治疗量异常的问题。

#3.2.1

修复同时跑多个战斗记录并且玩家发生过变化时，程序有概率崩溃的问题。

修复走火入魔有可能出现在非玩家目标上从而导致程序崩溃的问题。

修复了奶歌复盘评分记录中BOSS名称填写成敖龙岛的问题。

修复了奶歌复盘中，天策与少林染色标反的问题。

#3.2.0

增加了英雄安小逢的演员复盘，包括各种承伤统计，入魔承疗，盯承伤。

增加范阳夜变奶歌的评分（暂用），略微调整显示格式。

现在默认的DPS覆盖率及破盾次数不再统计厌夜，而是统计安小逢。

区分普通与英雄的范阳夜变，在图片中显示。

修改config.ini的格式，现在可以在其中设定是否进行奶歌复盘和演员复盘了。

修复了部分系统喊话为空时，会让程序崩溃的问题。

#3.1.0

加入了犯错统计，显示在演员复盘的右边。

增加迟驻的伤害统计、debuff统计和真实伤害折算。

增加白某的锁链统计。

自动寻找BOSS时，不再把相邻的BOSS推测成缺失的。

修复了少林和天策职业染色标反的问题。

#3.0.0

支持了新版本的茗伊复盘数据，现在可以正确识别喊话、进战记录等数据，避免崩溃。

增加了英雄厌夜的承伤统计（暂时处于测试阶段）。

#2.3.0

修复了在统计全程数据时，由于ID不一致可能导致统计失败的问题。（对体服数据或小号特别明显）

为范阳夜变增加统计，记录2,3,4的贴盾数据。

#2.2.0

修复了盾数的计算。现在会统计风雷盾，并且可以统计上盾技能丢失时（例如开战前贴盾）的情形。

#2.1.0

添加了文字输出模式。在config.ini中设置text=1，即可输出文字版的统计结果到result.txt中。

将APS（每秒化解）从HPS中独立出来，成为一个单独的统计数据。

为HPS统计添加了比例和排名。

修复了NPC治疗量显示为0的问题，并显示总治疗人数。

为是否染色在config.ini中开启一个选项。

为范阳夜变的BOSS添加了识别接口，现在可以识别对应的五个BOSS了。但体服的路径无法自动获取，必须手动找到文件。

#2.0.2

修复了老四NPC治疗量不正确的问题。

#2.0.1

修复了文本描述中，角色ID显示为数字的问题。

#2.0.0

匹配了最新的茗伊战斗复盘格式，现在可以分析5.5之后生成的复盘数据了。

增加了门派染色功能，现在对团队中的统计，会自动对门派染色了。

加入了盾每分的统计。现在的评分系统中，会改为使用盾每分来进行评分，相应的指标也有所变化。

加入老五连线次数统计，并在连线时对评分进行补偿。

修复了覆盖率接近100%时会计算为0的问题。

修复了老六心狐炸人时不计算的问题。

修复了评分系统中，重伤的-2计算为-1的问题。

#1.8.0

新增了打分系统，当BOSS数量=6时，会对全程的战斗情况进行打分。

略微调整了界面的格式。

#1.7.3

犯错记录加入零域。

#1.7.2

修复了全程不犯错时程序会崩溃的问题。

#1.7.1

犯错记录中，被抵挡的技能不再计算在内（例如山河）。

#1.7.0

增加了演员数据统计功能。现在会在奶歌战斗记录中生成自己的演员数据了。（完整的演员统计会在之后的版本中更新）

#1.6.4

修复了有战斗为整数分钟的时候，无法生成图片的BUG。

#1.6.3

修复多个BOSS的情况下，前面的BOSS会影响后面BOSS空闲比例的问题。

#1.6.2

修复了加速导入不正确的问题，现在可以正常设置加速从而判定空闲比例了。（3770的默认情况也可能会有一些BUG，已修复）

#1.6.1

修复了DPS监控不正确的问题，现在对DPS的标准更严格了（>10000，从而会减少DPS数量，相对地覆盖率会变高很多）。

战斗时间现在会以x分x秒的形式显示。

#1.6.0

定义并生成空闲比例，这是一个新的指标，可以看到自己在不同BOSS中“无事可做”的时间。

修复了会把自己算成一个DPS从而影响覆盖率与破盾数量的问题。

监控了风雷盾的buff，算作原本的覆盖率、DPS统计与破盾数的记录（DPS提升仍算作13.9%）

修复第一次运行时报错的问题。现在生成配置文件后会直接退出。

更新了几个常见错误的解决方案。

#1.5.2

读取config.ini时同时尝试使用gbk进行解析。

#1.5.1

生成config.ini的时候默认用utf-8生成，以解决部分时候自动生成的config.ini无法使用的问题。

#1.5.0

修改对战斗前梅花三弄的推测逻辑，现在也会记录梅花三弄技能本身的数据。

（这可能会导致一些BOSS的覆盖率发生变化，特别是老三这种技能频率本身不高的BOSS）

修复了当有DPS全程没有被套过盾时，程序会崩溃的问题。

增加了字体读取模块，现在在找不到系统自带的微软雅黑字体时，会尝试在当前目录下查找。

修复了异常处理机制，现在在出现异常时不会闪退，而是会把信息留在屏幕上。


#1.4.2

在分析结束后要求按任意键才能结束，以保留错误记录。

#1.4.1

修复了不指定奶歌ID时会导致除老一外的所有BOSS无法识别奶歌位置的BUG。

#1.4.0

重新调整配置文件格式。现在在运行脚本时如果目录下并没有配置文件，则会生成一个默认配置文件。

新增指定奶歌ID功能。在有多个奶歌时，可以在配置文件中指定奶歌ID从而进行分析。

新增ID打码功能。在配置文件中进行设置即可将ID打码。

修复了一个会导致开场时的盾监控不正确的BUG。

#1.3.0

加入目录自动查找功能。在指定记录者角色名的情况下，可以自动查找剑三的位置，并自动生成最近一次的战斗记录。

提供了配置文件，可以人工指定剑三的安装位置或战斗记录的存放位置。

##1.2.2

修复了特殊情况下梅花盾的时间监控会导致程序崩溃的BUG。

##1.2.1

修复平均覆盖率无法显示的BUG。

修复玩家ID没有移除双引号的BUG。

##1.2.0

使用面向对象的方式重构代码，增加可读性。

修复了开战之前的梅花三弄不计入统计的问题，会影响一些BOSS的覆盖率。

##1.1.0 

正确识别队里的奶歌（排除莫问的影响）。

略微调整格式，防止文本覆盖。

加入测试QQ群号和生成日期。

在每个HPS统计中加入战斗时间。

##1.0.1 

调整覆盖率与破盾次数统计的高度。

##1.0.0 

世界线的开始。