# Created by moeheart at 10/17/2021
# 雷域大泽6号-乌蒙贵的复盘库。

from replayer.boss.Base import SpecificReplayerPro, SpecificBossWindow, ToolTip
from replayer.BattleHistory import BattleHistory
from replayer.TableConstructorMeta import TableConstructorMeta
from replayer.utils import CriticalHealCounter, DpsShiftWindow
from tools.Functions import *
from Constants import *

import tkinter as tk
        
class WuMengguiWindow(SpecificBossWindow):
    '''
    乌蒙贵复盘窗口类。
    '''

    def loadWindow(self):
        '''
        使用tkinter绘制详细复盘窗口。
        '''
        window = tk.Toplevel()
        #window = tk.Tk()
        window.title('乌蒙贵复盘')
        window.geometry('1200x800')
        
        frame1 = tk.Frame(window)
        frame1.pack()
        
        #通用格式：
        #0 ID, 1 门派, 2 有效DPS, 3 团队-心法DPS/治疗量, 4 装分, 5 详情, 6 被控时间
        
        tb = TableConstructorMeta(self.config, frame1)
        
        tb.AppendHeader("玩家名", "", width=13)
        tb.AppendHeader("有效DPS", "全程DPS。与游戏中不同的是，重伤时间也会被计算在内。")
        tb.AppendHeader("团队-心法DPS", "综合考虑当前团队情况与对应心法的全局表现，计算的百分比。平均水平为100%。")
        tb.AppendHeader("装分", "玩家的装分，可能会获取失败。")
        tb.AppendHeader("详情", "装备详细描述，暂未完全实装。")
        tb.AppendHeader("强化", "装备强化列表，表示[精炼满级装备数量]/[插8]-[插7]-[插6]/[五彩石等级]/[紫色附魔]-[蓝色附魔]/[大附魔：手腰脚头衣裤]")
        tb.AppendHeader("被控", "受到影响无法正常输出的时间，以秒计。")
        tb.AppendHeader("P1DPS", "对P1乌蒙贵的输出，通常战斗流程中不会有这个阶段。\n阶段持续时间：%s"%parseTime(self.detail["P1Time"]))
        tb.AppendHeader("P2BOSS", "对P2黑条巨蛾的输出。\n阶段持续时间：%s"%parseTime(self.detail["P2Time"]))
        tb.AppendHeader("触手有效", "对P2触手的输出，错误触手的输出不计入，但猜测正确的计入。\n分母按P2持续时间计算。")
        tb.AppendHeader("触手首次", "对P2第一个激活的触手的输出。\n分母按P2持续时间计算。")
        tb.AppendHeader("蛾卵DPS", "对P2蛾卵的输出。\n分母按P2持续时间计算。")
        tb.AppendHeader("P3DPS", "对P3乌蒙贵的输出，使用复盘分析化解的伤害。")
        tb.AppendHeader("P3存活时间", "在P3的存活时间，以秒计。")
        tb.AppendHeader("P3中圈", "P3中猛毒雷电圈的次数。")
        tb.AppendHeader("心法复盘", "心法专属的复盘模式，只有很少心法中有实现。")
        tb.EndOfLine()
        
        for i in range(len(self.effectiveDPSList)):
            name = self.getMaskName(self.effectiveDPSList[i][0])
            color = getColor(self.effectiveDPSList[i][1])
            tb.AppendContext(name, color=color, width=13)
            tb.AppendContext(int(self.effectiveDPSList[i][2]))

            if getOccType(self.effectiveDPSList[i][1]) != "healer":
                text3 = str(self.effectiveDPSList[i][3]) + '%'
                color3 = "#000000"
            else:
                text3 = self.effectiveDPSList[i][3]
                color3 = "#00ff00"
            tb.AppendContext(text3, color=color3)
            
            text4 = "-"
            if self.effectiveDPSList[i][4] != -1:
                text4 = int(self.effectiveDPSList[i][4])
            color4 = "#000000"
            if "大橙武" in self.effectiveDPSList[i][5]:
                color4 = "#ffcc00"
            tb.AppendContext(text4, color=color4)
            
            tb.AppendContext(self.effectiveDPSList[i][5].split('|')[0])
            tb.AppendContext(self.effectiveDPSList[i][5].split('|')[1])
            tb.AppendContext(int(self.effectiveDPSList[i][6]))

            tb.AppendContext(int(self.effectiveDPSList[i][7]))
            tb.AppendContext(int(self.effectiveDPSList[i][8]))
            tb.AppendContext(int(self.effectiveDPSList[i][9]))
            tb.AppendContext(int(self.effectiveDPSList[i][10]))
            tb.AppendContext(int(self.effectiveDPSList[i][11]))
            tb.AppendContext(int(self.effectiveDPSList[i][12]))
            tb.AppendContext(int(self.effectiveDPSList[i][13]))

            color14 = "#000000"
            if self.effectiveDPSList[i][14] > 0:
                color14 = "#ff0000"
            tb.AppendContext(int(self.effectiveDPSList[i][14]), color=color14)

            # 心法复盘
            if self.effectiveDPSList[i][0] in self.occResult:
                tb.GenerateXinFaReplayButton(self.occResult[self.effectiveDPSList[i][0]], self.effectiveDPSList[i][0])
            else:
                tb.AppendContext("")
            tb.EndOfLine()

        frame2 = tk.Frame(window)
        frame2.pack()
        buttonPrev = tk.Button(frame2, text='<<', width=2, height=1, command=self.openPrev)
        submitButton = tk.Button(frame2, text='战斗事件记录', command=self.openPot)
        buttonNext = tk.Button(frame2, text='>>', width=2, height=1, command=self.openNext)
        buttonPrev.grid(row=0, column=0)
        submitButton.grid(row=0, column=1)
        buttonNext.grid(row=0, column=2)

        self.window = window
        window.protocol('WM_DELETE_WINDOW', self.final)

    def __init__(self, config, effectiveDPSList, detail, occResult):
        super().__init__(config, effectiveDPSList, detail, occResult)

class WuMengguiReplayer(SpecificReplayerPro):

    def countFinal(self):
        '''
        战斗结束时需要处理的流程。包括BOSS的通关喊话和全团脱战。
        '''
        # 结算触手伤害
        for line2 in self.chushou:
            for line in self.chushou[line2]["dps"]:
                self.stat[line][9] += self.chushou[line2]["dps"][line]
                if self.finalTime - self.chushouLastTime > 60000:
                    self.stat[line][10] += self.chushou[line2]["dps"][line]
        # 结算P3存活时间
        if self.phase == 3:
            for line in self.bld.info.player:
                if self.alive[line] == 1:
                    self.stat[line][13] = int((self.finalTime - self.phaseStart) / 1000)
        # 计算阶段时间
        self.phaseTime[self.phase] += self.finalTime - self.phaseStart

        self.detail["P1Time"] = int((self.phaseTime[1]) / 1000)
        self.detail["P2Time"] = int(self.phaseTime[2] / 1000)
        self.detail["P3Time"] = int(self.phaseTime[3] / 1000)

        for line in self.zc:
            self.bh.setEnvironment("28745", "振翅", "4718", line[0], line[1]-line[0], 1, "")
        for line in self.cs:
            self.bh.setEnvironment("0", "触手", "922", line[0], line[1]-line[0], 1, "")

    def getResult(self):
        '''
        生成复盘结果的流程。需要维护effectiveDPSList, potList与detail。
        '''

        self.countFinal()

        bossResult = []
        for id in self.bld.info.player:
            if id in self.stat:
                line = self.stat[id]
                if id in self.equipmentDict:
                    line[4] = self.equipmentDict[id]["score"]
                    line[5] = "%s|%s"%(self.equipmentDict[id]["sketch"], self.equipmentDict[id]["forge"])
                else:
                    line[5] = "|"
                
                if getOccType(self.occDetailList[id]) == "healer":
                    line[3] = int(self.hps[id] / self.battleTime * 1000)

                dps = int(line[2] / self.battleTime * 1000)
                bossResult.append([line[0],
                                   line[1],
                                   dps, 
                                   line[3],
                                   line[4],
                                   line[5],
                                   line[6],
                                   int(line[7] / (self.detail["P1Time"] + 1e-10)),
                                   int(line[8] / (self.detail["P2Time"] + 1e-10)),
                                   int(line[9] / (self.detail["P2Time"] + 1e-10)),
                                   int(line[10] / (self.detail["P2Time"] + 1e-10)),
                                   int(line[11] / (self.detail["P2Time"] + 1e-10)),
                                   int(line[12] / (self.detail["P3Time"] + 1e-10)),
                                   line[13],
                                   line[14],
                                   ])
        bossResult.sort(key=lambda x: -x[2])
        self.effectiveDPSList = bossResult

        return self.effectiveDPSList, self.potList, self.detail
        
    def recordDeath(self, item, deathSource):
        '''
        在有玩家重伤时的额外代码。
        params
        - item 复盘数据，意义同茗伊复盘。
        - deathSource 重伤来源。
        '''
        pass

    def analyseSecondStage(self, event):
        '''
        处理单条复盘数据时的流程，在第二阶段复盘时，会以时间顺序不断调用此方法。
        params
        - item 复盘数据，意义同茗伊复盘。
        '''

        if event.dataType == "Skill":
            if event.target in self.bld.info.player:
                if event.heal > 0 and event.effect != 7 and event.caster in self.hps:  # 非化解
                    self.hps[event.caster] += event.healEff
                if event.target in self.stat and event.id == "27828" and event.damageEff > 0:  # 猛毒雷电
                    self.stat[event.target][14] += 1
                if event.id in ["28745"]:  # 振翅
                    if event.time - self.zc[-1][1] > 5000:
                        self.zc.append([event.time - 1000, event.time, self.phase])
                    elif event.time - self.zc[-1][1] > 100:
                        self.zc[-1][1] = event.time
                    
            else:
                if event.caster in self.bld.info.player and event.caster in self.stat:
                    self.stat[event.caster][2] += event.damageEff
                    if event.target in self.bld.info.npc:
                        if self.bld.info.npc[event.target].name in ["乌蒙贵", "烏蒙貴"] and self.phase == 1:
                                self.stat[event.caster][7] += event.damageEff
                        elif self.bld.info.npc[event.target].name in ["黑条巨蛾", "黑條巨蛾"]:
                            self.stat[event.caster][8] += event.damageEff
                            if event.damageEff > 0 and self.phase == 1:
                                self.phaseTime[1] = event.time - self.phaseStart
                                self.phase = 2
                                self.phaseStart = event.time
                        elif self.bld.info.npc[event.target].name in ["触手", "觸手"]:
                            self.chushou[event.target]["dps"][event.caster] += event.damageEff
                        elif self.bld.info.npc[event.target].name in ["蛾卵"]:
                            self.stat[event.caster][11] += event.damageEff
                        elif self.bld.info.npc[event.target].name in ["乌蒙贵", "烏蒙貴"] and self.phase == 3:
                            self.stat[event.caster][12] += int(event.fullResult.get("9", 0))

                    if (event.damageEff > 0 or event.healEff > 0) and event.scheme == 1:
                        self.alive[event.caster] = 1
                
        elif event.dataType == "Buff":
            if event.target not in self.bld.info.player:
                return

            if event.id in ["8510"]:  # 好团长点赞
                self.win = 1
                    
        elif event.dataType == "Shout":
            if event.content in ['"呵呵呵呵呵……哈哈哈哈哈……这就是毒神的力量！"', '"呵呵呵呵呵……哈哈哈哈哈……這就是毒神的力量！"']:
                self.phaseTime[2] = event.time - self.phaseStart
                self.phase = 3
                self.phaseStart = event.time
                self.bh.setEnvironment("0", "毒神形态", "2129", event.time-10000, 10000, 1, "")

        elif event.dataType == "Death":  # 重伤记录
            if event.id in self.bld.info.player:
                self.alive[event.id] = 0
                if self.phase == 3:
                    self.stat[event.id][13] = int((event.time - self.phaseStart) / 1000)

            if event.id in self.bld.info.npc and self.bld.info.npc[event.id].name in ["触手", "觸手"]:
                # 结算触手伤害
                for line2 in self.chushou:
                    for line in self.chushou[line2]["dps"]:
                        if line2 == event.id:
                            self.stat[line][9] += self.chushou[line2]["dps"][line]
                            if event.time - self.chushouLastTime > 60000:
                                self.stat[line][10] += self.chushou[line2]["dps"][line]
                        self.chushou[line2]["dps"][line] = 0
                self.chushouLastTime = event.time
                self.chushouNum -= 1
                if self.chushouNum == 0:
                    self.cs[-1][1] = event.time

        elif event.dataType == "Battle":  # 战斗状态变化
            pass

        elif event.dataType == "Scene":  # 进入、离开场景
            if event.id in self.bld.info.npc and self.bld.info.npc[event.id].name in ["乌蒙贵"] and event.enter == 0:
                self.win = 1
            if event.id in self.bld.info.npc and self.bld.info.npc[event.id].name in ["触手"] and event.enter:
                if event.time - self.cs[-1][0] > 10000:
                    self.cs.append([event.time, self.finalTime])
                    self.chushouNum = 4
                    
    def analyseFirstStage(self, item):
        '''
        处理单条复盘数据时的流程，在第一阶段复盘时，会以时间顺序不断调用此方法。
        params
        - item 复盘数据，意义同茗伊复盘。
        '''
        pass


    def initBattle(self):
        '''
        在战斗开始时的初始化流程，当第二阶段复盘开始时运行。
        '''
        self.activeBoss = "乌蒙贵"
        
        # 通用格式：
        # 0 ID, 1 门派, 2 有效DPS, 3 团队-心法DPS/治疗量, 4 装分, 5 详情, 6 被控时间

        # 乌蒙贵数据格式：
        # 7 P1DPS, 8 P2BOSS, 9 触手有效, 10 触手首次, 11 蛾卵DPS, 12 P3DPS, 13 P3存活时间, 14 P3中圈
        
        self.stat = {}
        self.hps = {}
        self.detail["boss"] = self.bossNamePrint
        self.win = 0
        self.alive = {}

        self.phase = 1
        self.phaseStart = self.startTime
        self.phaseTime = [0, 0, 0, 0]

        self.bh = BattleHistory(self.startTime, self.finalTime)
        self.hasBh = True
        self.zc = [[0, 0, 0]]  # 振翅
        self.cs = [[0, 0]]  # 触手
        
        for line in self.bld.info.player:
            self.hps[line] = 0
            self.stat[line] = [self.bld.info.player[line].name, self.occDetailList[line], 0, 0, -1, "", 0] + \
                [0, 0, 0, 0, 0, 0, 0, 0]
            self.alive[line] = 0

        # 统计触手
        self.chushou = {}
        self.chushouNum = 0
        self.chushouLastTime = 0
        for line2 in self.bld.info.npc:
            if self.bld.info.npc[line2].name in ["触手", "觸手"]:
                self.chushou[line2] = {"dps": {}, "status": 0, "time": 0}
                for line in self.bld.info.player:
                    self.chushou[line2]["dps"][line] = 0

    def __init__(self, bld, occDetailList, startTime, finalTime, battleTime, bossNamePrint):
        '''
        对类本身进行初始化。
        '''
        super().__init__(bld, occDetailList, startTime, finalTime, battleTime, bossNamePrint)

