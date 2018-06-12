# -*-coding:utf-8-*-
from linepy import *
from akad.ttypes import Message
from time import sleep
import time, sys, random, json, codecs


cl = LINE("puc1tr9oqhpe@sute.jp", "Towas0328")
channelToken = cl.getChannelResult()
cl.log("TOKEN:" + str(cl.authToken))
k1 = LINE("tqsbm025mvwu@sute.jp", "Towas0328")
channelToken = k1.getChannelResult()
k1.log("TOKEN:" + str(k1.authToken))
k2 = LINE("u5mkv8t71l8h@sute.jp", "Towas0328")
k2.log("TOKEN:" + str(k2.authToken))
k3 = LINE("a4kd3fa1b41w@sute.jp", "Towas0328")
channelToken = k3.getChannelResult()
k3.log("TOKEN:" + str(k3.authToken))
k4 = LINE("io4l65a0aocm@sute.jp", "Towas0328")
channelToken = k4.getChannelResult()
k4.log("TOKEN:" + str(k4.authToken))

print ("=n=e=g=i=n=i=r=a=n=!=")

wait={
    'black':{},
    'wblack':{},
    'dblack':{},
    'pname':{},
    'pro_name':{},
    'pinv':{},
    'pkick':{},
    'purl':{},
    'pc':{},
    'pp':{},
    'mute':{}
    }

f = codecs.open('crsblack.json', 'r', 'utf-8')
wait['black'] = json.load(f)
f.close()

help1 = """neginiran-bot@v5.0.1

※一般権限者は以下のコマンドが利用出来ます
《Negi:ヘルプ》
──
「Negi:オン」ねぎにらんを喋らせます。
「Negi:オフ」ねぎにらんを黙らせます。
──
「Negi:生存確認」キッカーの生存確認をします。
「Negi:再雇用」足りないキッカーを、取り戻す。
「Negi:解雇」ねぎにらんを追い出します。
「Negi:速度」botの速度を表示します。
──
「設定:ヘルプ」グループ内の設定に関するヘルプを表示します。
──
──
※最高権限者は以下のコマンドが利用出来ます
──
「設定:ブラック追加」連絡先でブラリスを追加します。
「設定:ブラック削除」連絡先でブラリスを削除します。
──
──
※管理者は以下のコマンドが利用出来ます
──
「権限追加 @」@で一般権限者を追加します
「権限削除 @」@で一般権限者を削除します
「最高追加 @」@で最高権限者を追加します
「最高削除 @」@で最高権限者を削除します
「全退会」ねぎにらんが全てのグループを退会します


権限購入は↓
http://line.me/ti/p/%40ubg0555p"""

help2 = """neginiran-bot@v5.0.1

※一般権限者は以下のコマンドが利用出来ます
《設定:ヘルプ》
──
「設定確認」保護関連の設定状況を確認します。
──
「招待URL生成」招待用のURLを生成します(´・ω・｀)
「招待URL許可」URL招待を許可します(´・ω・｀)
「招待URL拒否」URL招待を拒否します(´・ω・｀)
──
「蹴り保護:オン」強制退会を禁止します(´・ω・｀)
「蹴り保護:オフ」強制退会を許可します(´・ω・｀)
「招待保護:オン」招待を禁止します(´・ω・｀)
「招待保護:オフ」招待を許可します(´・ω・｀)
「URL保護:オン」URL招待を禁止します(´・ω・｀)
「URL保護:オフ」URL招待を許可します(´・ω・｀)
「画像保護:オン」グル画変更を禁止します(´・ω・｀)
「画像保護:オフ」グル画変更を許可します(´・ω・｀)
「名前保護:オン」グル名変更を禁止します(´・ω・｀)
「名前保護:オフ」グル名変更を許可します(´・ω・｀)
「キャンセル保護:オン」招待のキャンセルを禁止します(´・ω・｀)
「キャンセル保護:オフ」招待のキャンセルを許可します(´・ω・｀)


権限購入は↓
http://line.me/ti/p/%40ubg0555p"""

admins=["ue0edee01d554184c78f2a5d68af285c8"]
f = open("crsadmins.txt","r")
for x in f:
    admins.append(x.rstrip("\n"))
f.close()
vertex=["ue0edee01d554184c78f2a5d68af285c8"]
f = open("vertex.txt","r")
for x in f:
    vertex.append(x.rstrip("\n"))
f.close()
negi=["ue0edee01d554184c78f2a5d68af285c8"]

oepoll = OEPoll(cl)
oepoll = OEPoll(k1)
oepoll = OEPoll(k2)
oepoll = OEPoll(k3)
oepoll = OEPoll(k4)
main = cl.getProfile().mid
ki1 = k1.getProfile().mid
ki2 = k2.getProfile().mid
ki3 = k3.getProfile().mid
ki4 = k4.getProfile().mid

bots = [cl,k1,k2,k3,k4]
bmids = [main,ki1,ki2,ki3,ki4]

def bot(op):
    try:
        if op.type == 11:
            if op.param3 == '4':
                if op.param1 in wait['purl']:
                    k = random.choice(bots)
                    if op.param2 in bmids:
                        pass
                    elif op.param2 in admins:
                        G = k.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k.updateGroup(G)
                    else:
                        G = k.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k.updateGroup(G)
                        k.kickoutFromGroup(op.param1, [op.param2])
                        M = Message()
                        M.text = None
                        M.contentType = 13
                        M.contentMetadata = {'mid':op.param2}
                        k.sendMessage(M)
                if op.param1 in wait ['pname']:
                    k = random.choice(bots)
                    if op.param2 in bmids:
                        pass
                    elif op.param2 in admins:
                        pass
                    else:
                        G = k.getGroup(op.param1)
                        G.name = wait['pro_name'][msg.to]
                        k.updateGroup(G)
                        k.kickoutFromGroup(op.param1, [op.param2])
                        M = Message()
                        M.text = None
                        M.contentType = 13
                        M.contentMetadata = {'mid':op.param2}
                        k.sendMessage(M)
        if op.type == 11:
            if op.param1 in wait ['pp']:
                k = random.choice(bots)
                if op.param2 in bmids:
                    pass
                elif op.param2 in admins:
                    pass
                else:
                    k.kickoutFromGroup(op.param1, [op.param2])
                    M = Message()
                    M.text = None
                    M.contentType = 13
                    M.contentMetadata = {'mid':op.param2}
                    k.sendMessage(M)
                else:
                    G = k.getGroup(op.param1)

        if op.type == 13:
            if main in op.param3:
                if op.param2 in admins:
                    cl.acceptGroupInvitation(op.param1)
                else:
                    cl.rejectGroupInvitation(op.param1)
            if ki1 in op.param3:
                if op.param2 in admins:
                    k1.acceptGroupInvitation(op.param1)
                else:
                    k1.rejectGroupInvitation(op.param1)
            if ki2 in op.param3:
                if op.param2 in admins:
                    k2.acceptGroupInvitation(op.param1)
                else:
                    k2.rejectGroupInvitation(op.param1)
            if ki3 in op.param3:
                if op.param2 in admins:
                    k3.acceptGroupInvitation(op.param1)
                else:
                    k3.rejectGroupInvitation(op.param1)
            if ki4 in op.param3:
                if op.param2 in admins:
                    k4.acceptGroupInvitation(op.param1)
                else:
                    k4.rejectGroupInvitation(op.param1)
            elif op.param1 in wait['pinv']:
                inv1 = op.param3.replace('\x1e',',')
                inv2 = inv1.split(',')
                cl.cancelGroupInvitation(op.param1, inv2)
            elif op.param1 in wait['black']:
                invb = []
                for i in op.param3:
                    for i in wait['black']:
                        invb.append(str(i))
                if invb == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, invb)
                    k = ransom.choice(bots)
                    k.sendMessage(op.param1, 'ブラリスです(´・ω・｀)')
                    M = Message()
                    M.text = None
                    M.contentType = 13
                    M.contentMetadata = {'mid':op.param1}
                    k.sendMessage(M)
        if op.type == 17:
            if op.param2 in wait['black']:
                kicker = random.choice(bots)
                try:
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
        if op.type == 19:
            if main in op.param3:
                if (op.param2 in admins) or (op.param2 in bmids):
                    try:
                        G = k1.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k1.updateGroup(G)
                        Ti = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ti)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                    except:
                        try:
                            G = k2.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k2.updateGroup(G)
                            Ti = k2.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            k2.updateGroup(G)
                        except:
                            try:
                                G = k3.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    k3.updateGroup(G)
                                Ti = k3.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1, Ti)
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    G = k4.getGroup(G)
                                    if G.preventedJoinByTicket == True:
                                        G.preventedJoinByTicket = False 
                                        k4.updateGroup(G)
                                    Ti = k4.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                                    G.preventedJoinByTicket = True
                                    k4.updateGroup(G)
                                except:
                                    pass
                else:
                    if op.param2 in wait['black']:
                        pass
                    else:
                        wait['black'][op.param2] = True
                        f = codecs.open('crsblack.json', 'w', 'utf-8')
                        json.dump(wait['black'], f, sort_keys = True, indent = 4, ensure_ascii = False)
                        f.close()
                        print (op.param2 + 'をブラックリストに追加しました。')
                    try:
                        G = k1.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k1.updateGroup(G)
                        Ti = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ti)
                        k1.kickoutFromGroup(op.param1, [op.param2])
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                    except:
                        try:
                            G = k2.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k2.updateGroup(G)
                            Ti = k2.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1, Ti)
                            k2.kickoutFromGroup(op.param1, [op.param2])
                            G.preventedJoinByTicket = True
                            k2.updateGroup(G)
                        except:
                            try:
                                G = k3.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    k3.updateGroup(G)
                                Ti = k3.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1, Ti)
                                k3.kickoutFromGroup(op.param1, [op.param2])
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    G = k4.getGroup(G)
                                    if G.preventedJoinByTicket == True:
                                        G.preventedJoinByTicket = False 
                                        k4.updateGroup(G)
                                    Ti = k4.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                                    k4.kickoutFromGroup(op.param1, [op.param2])
                                    G.preventedJoinByTicket = True
                                    k4.updateGroup(G)
                                except:
                                    pass
            if ki1 in op.param3:
                if (op.param2 in admins) or (op.param2 in bmids):
                    try:
                        G = k2.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k2.updateGroup(G)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k1.acceptGroupInvitationByTicket(op.param1, Ti)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                    except:
                        try:
                            G = k3.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k3.updateGroup(G)
                            Ti = k3.reissueGroupTicket(op.param1)
                            k1.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            k3.updateGroup(G)
                        except:
                            try:
                                G = k4.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    k4.updateGroup(G)
                                Ti = k4.reissueGroupTicket(op.param1)
                                k1.acceptGroupInvitationByTicket(op.param1, Ti)
                                G.preventedJoinByTicket = True
                                k4.updateGroup(G)
                            except:
                                try:
                                    G = cl.getGroup(G)
                                    if G.preventedJoinByTicket == True:
                                        G.preventedJoinByTicket = False
                                        cl.updateGroup(G)
                                    Ti = cl.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1, Ti)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                except:
                                    pass
                else:
                    if op.param2 in wait['black']:
                        pass
                    else:
                        wait['black'][op.param2] = True
                        f = codecs.open('crsblack.json', 'w', 'utf-8')
                        json.dump(wait['black'], f, sort_keys = True, indent = 4, ensure_ascii = False)
                        f.close()
                        print (op.param2 + 'をブラックリストに追加しました。')
                    try:
                        G = k2.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k2.updateGroup(G)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k1.acceptGroupInvitationByTicket(op.param1, Ti)
                        k2.kickoutFromGroup(op.param1, [op.param2])
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                    except:
                        try:
                            G = k3.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k3.updateGroup(G)
                            Ti = k3.reissueGroupTicket(op.param1)
                            k1.acceptGroupInvitationByTicket(op.param1, Ti)
                            k3.kickoutFromGroup(op.param1, [op.param2])
                            G.preventedJoinByTicket = True
                            k3.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k1.acceptGroupInvitationByTicket(op.param1, Ti)
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                try:
                                    G = k4.getGroup(G)
                                    if G.preventedJoinByTicket == True:
                                        G.preventedJoinByTicket = False
                                        k4.updateGroup(G)
                                    Ti = k4.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1, Ti)
                                    k4.kickoutFromGroup(op.param1, [op.param2])
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                except:
                                    pass
            if ki2 in op.param3:
                if (op.param2 in admins) or (op.param2 in bmids):
                    try:
                        G = k3.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k3.updateGroup(G)
                        Ti = k3.reissueGroupTicket(op.param1)
                        k2.acceptGroupInvitationByTicket(op.param1, Ti)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                    except:
                        try:
                            G = k1.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                            Ti = k1.reissueGroupTicket(op.param1)
                            k2.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            k1.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k2.acceptGroupInvitationByTicket(op.param1, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                pass
                else:
                    if op.param2 in wait['black']:
                        pass
                    else:
                        wait['black'][op.param2] = True
                        f = codecs.open('crsblack.json', 'w', 'utf-8')
                        json.dump(wait['black'], f, sort_keys = True, indent = 4, ensure_ascii = False)
                        f.close()
                        print (op.param2 + 'をブラックリストに追加しました。')
                    try:
                        G = k3.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k3.updateGroup(G)
                        Ti = k3.reissueGroupTicket(op.param1)
                        k2.acceptGroupInvitationByTicket(op.param1, Ti)
                        k3.kickoutFromGroup(op.param1, [op.param2])
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                    except:
                        try:
                            G = k1.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                            Ti = k1.reissueGroupTicket(op.param1)
                            k2.acceptGroupInvitationByTicket(op.param1, Ti)
                            k1.kickoutFromGroup(op.param1, [op.param2])
                            G.preventedJoinByTicket = True
                            k1.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k2.acceptGroupInvitationByTicket(op.param1, Ti)
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                pass
            if ki3 in op.param3:
                if (op.param2 in admins) or (op.param2 in bmids):
                    try:
                        G = k2.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k2.updateGroup(G)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k3.acceptGroupInvitationByTicket(op.param1, Ti)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                    except:
                        try:
                            G = k1.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                            Ti = k1.reissueGroupTicket(op.param1)
                            k3.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            k1.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k3.acceptGroupInvitationByTicket(op.param1, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                pass
                else:
                    if op.param2 in wait['black']:
                        pass
                    else:
                        wait['black'][op.param2] = True
                        f = codecs.open('crsblack.json', 'w', 'utf-8')
                        json.dump(wait['black'], f, sort_keys = True, indent = 4, ensure_ascii = False)
                        f.close()
                        print (op.param2 + 'をブラックリストに追加しました。')
                    try:
                        G = k2.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k2.updateGroup(G)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k3.acceptGroupInvitationByTicket(op.param1, Ti)
                        k2.kickoutFromGroup(op.param1, [op.param2])
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                    except:
                        try:
                            G = k1.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                            Ti = k1.reissueGroupTicket(op.param1)
                            k3.acceptGroupInvitationByTicket(op.param1, Ti)
                            k1.kickoutFromGroup(op.param1, [op.param2])
                            G.preventedJoinByTicket = True
                            k1.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k3.acceptGroupInvitationByTicket(op.param1, Ti)
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                pass
            if ki4 in op.param3:
                if (op.param2 in admins) or (op.param2 in bmids):
                    try:
                        G = k2.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k2.updateGroup(G)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k4.acceptGroupInvitationByTicket(op.param1, Ti)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                    except:
                        try:
                            G = k1.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                            Ti = k1.reissueGroupTicket(op.param1)
                            k4.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            k1.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k4.acceptGroupInvitationByTicket(op.param1, Ti)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                pass
                else:
                    if op.param2 in wait['black']:
                        pass
                    else:
                        wait['black'][op.param2] = True
                        f = codecs.open('crsblack.json', 'w', 'utf-8')
                        json.dump(wait['black'], f, sort_keys = True, indent = 4, ensure_ascii = False)
                        f.close()
                        print (op.param2 + 'をブラックリストに追加しました。')
                    try:
                        G = k2.getGroup(op.param1)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            k2.updateGroup(G)
                        Ti = k2.reissueGroupTicket(op.param1)
                        k4.acceptGroupInvitationByTicket(op.param1, Ti)
                        k2.kickoutFromGroup(op.param1, [op.param2])
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                    except:
                        try:
                            G = k1.getGroup(G)
                            if G.preventedJoinByTicket == True:
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                            Ti = k1.reissueGroupTicket(op.param1)
                            k4.acceptGroupInvitationByTicket(op.param1, Ti)
                            k1.kickoutFromGroup(op.param1, [op.param2])
                            G.preventedJoinByTicket = True
                            k1.updateGroup(G)
                        except:
                            try:
                                G = cl.getGroup(G)
                                if G.preventedJoinByTicket == True:
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                Ti = cl.reissueGroupTicket(op.param1)
                                k4.acceptGroupInvitationByTicket(op.param1, Ti)
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                            except:
                                pass
            if op.param1 in wait['pkick']:
                if (op.param2 in bmids) or (op.param2 in admins):
                    pass
                else:
                    k = random.choice(bots)
                    k.kickoutFromGroup(op.param1, [op.param2])
                    M = Message()
                    M.text = None
                    M.contentType = 13
                    M.contentMetadata = {'mid':op.param2}
                    k.sendMessage(M)
        if op.type == 32:
            if op.param1 in wait["pc"]:
                if (op.param2 in bmids) or (op.param2 in admins):
                    pass
                else:
                    k = random.choice(bots)
                    k.cancelGroupInvitation(op.param1,[op.param3])
                    k.kickoutFromGroup(op.param1,[op.param2])
                    M = Message()
                    M.text = None
                    M.contentType = 13
                    M.contentMetadata = {'mid':op.param2}
                    k.sendMessage(M)
        if op.type == 26:
            msg = op.message
            t = random.choice(bots)
            if msg._from in negi:
                if msg.contentType == 0:
                    if '権限追加 ' in msg.text:
                        if msg.contentMetadata is not None:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                con = cl.getContact(target)
                                if target in admins:
                                    t.sendMessage(msg.to, "既に権限者です")
                                else:
                                    admins.append(target)
                                    t.sendMessage(msg.to, "権限者に追加しました")
                            f = open('crsadmins.txt', 'w')
                            for x in admins:
                                f.write(str(x) + "\n")
                            f.close()
                        else:
                            pass
                    if '権限削除 ' in msg.text:
                        if msg.contentMetadata is not None:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                con = cl.getContact(target)
                                if target in admins:
                                    admins.remove(target)
                                    t.sendMessage(msg.to,con.displayName + "を権限者から外しました")
                                else:
                                    t.sendMessage(msg.to,con.displayName + "は権限者ではありません")
                            f = open('crsadmins.txt', 'w')
                            for x in admins:
                                f.write(str(x) + "\n")
                            f.close()
                        else:
                            pass
                    if '最高追加 ' in msg.text:
                        if msg.contentMetadata is not None:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                con = cl.getContact(target)
                                if target in vertex:
                                    t.sendMessage(msg.to, "既に最高権限者です")
                                else:
                                    vertex.append(target)
                                    t.sendMessage(msg.to, "最高権限者に追加しました")
                            f = open('vertex.txt', 'w')
                            for x in vertex:
                                f.write(str(x) + "\n")
                            f.close()
                        else:
                            pass
                    if '最高削除 ' in msg.text:
                        if msg.contentMetadata is not None:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                con = cl.getContact(target)
                                if target in vertex:
                                    vertex.remove(target)
                                    t.sendMessage("最高権限を剥奪しました")
                                else:
                                    t.sendMessage(msg.to,con.displayName + "は最高権限者ではありません")
                            f = open('vertex.txt', 'w')
                            for x in vertex:
                                f.write(str(x) + "\n")
                            f.close()
                        else:
                            pass
                    if msg.text in ["全退会"]:
                        gid = cl.getGroupIdsJoined()
                        for i in gid:
                            cl.leaveGroup(i)
                            k1.leaveGroup(i)
                            k2.leaveGroup(i)
                            k3.leaveGroup(i)
                            k4.leaveGroup(i)
            if msg._from in admins:
                if msg.contentType == 0:
                    if "Negi:オフ" == msg.text:
                        if msg.to in wait["mute"]:
                            pass
                        else:
                            wait["mute"][msg.to] = True
                            t.sendMessage(msg.to, "トーク反応をオフにしました(´・ω・｀)")
                    if "Negi:オン" == msg.text:
                        if msg.to in wait["mute"]:
                            del wait["mute"][msg.to]
                            t.sendMessage(msg.to, "トーク反応をオンにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                    if "Negi:ヘルプ" == msg.text:
                        t.sendMessage(msg.to, help1)
                    if "設定:ヘルプ" == msg.text:
                        t.sendMessage(msg.to, help2)
                    if msg.to in wait["mute"]:
                        return
                    elif msg.text in ["招待URL生成"]:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            if group.preventedJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to, "招待URLを生成したよ☆\n(※今までにねぎにらんが発行したURLは使えなくなりました。)\n\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                            else:
                                cl.sendMessage(msg.to, "招待URLを生成したよ☆\n(※今までにねぎにらんが発行したURLは使えなくなりました。)\n\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                    elif msg.text in ["招待URL許可"]:
                        if msg.toType == 2:
                            G = cl.getGroup(msg.to)
                            if G.preventedJoinByTicket == False:
                                cl.sendMessage(msg.to, "既に許可されています")
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                cl.sendMessage(msg.to, "許可しました")
                    elif msg.text in ["招待URL拒否"]:
                        if msg.toType == 2:
                            G = cl.getGroup(msg.to)
                            if G.preventedJoinByTicket == True:
                                cl.sendMessage(msg.to, "既に拒否されています")
                            else:
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                cl.sendMessage(msg.to, "拒否しました")
                    elif msg.text == "mid":
                        cl.sendMessage(msg.to, msg._from)
                    elif "Negi:生存確認" == msg.text:
                        cl.sendMessage(msg.to, "client異常なし")
                        k1.sendMessage(msg.to, "kicker異常なし")
                        k2.sendMessage(msg.to, "kicker2異常なし")
                        k3.sendMessage(msg.to, "kicker3異常なし")
                        k4.sendMessage(msg.to, "kicker4異常なし")
                    elif "Negi:速度" == msg.text:
                        start = time.time()
                        t.sendMessage(msg.to, "うーん、このbotの速度は…")
                        elapsed_time = time.time() - start
                        cl.sendMessage(msg.to, "%ssecかな〜" % (elapsed_time))
                    elif "Negi:再雇用" == msg.text:
                        G = cl.getGroup(msg.to)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                        Ti = cl.reissueGroupTicket(msg.to)
                        k1.acceptGroupInvitationByTicket(msg.to, Ti)
                        k2.acceptGroupInvitationByTicket(msg.to, Ti)
                        k3.acceptGroupInvitationByTicket(msg.to, Ti)
                        k4.acceptGroupInvitationByTicket(msg.to, Ti)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                    elif "名前保護:オン" == msg.text:
                        if msg.to in wait["pname"]:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                        else:
                            wait["pname"][msg.to] = True
                            G = k.getGroup(msg.to)
                            wait["pro_name"][msg.to] = G.name
                            t.sendMessage(msg.to, "グル名保護をオンにしました(´・ω・｀)")
                    elif "名前保護:オフ" == msg.text:
                        if msg.to in wait['pname']:
                            del wait['pname'][msg.to]
                            del wait['pro_name'][msg.to]
                            t.sendMessage(msg.to, "グル名保護をオフにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオフです(´・ω・｀)")
                    elif "招待保護:オン" == msg.text:
                        if msg.to in wait["pinv"]:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                        else:
                            wait["pinv"][msg.to] = True
                            t.sendMessage(msg.to, "招待保護をオンにしました(´・ω・｀)")
                    elif "招待保護:オフ" == msg.text:
                        if msg.to in wait['pinv']:
                            del wait['pinv'][msg.to]
                            t.sendMessage(msg.to, "招待保護をオフにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオフです(´・ω・｀)")
                    elif "蹴り保護:オン" == msg.text:
                        if msg.to in wait["pkick"]:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                        else:
                            wait["pkick"][msg.to] = True
                            t.sendMessage(msg.to, "蹴り保護をオンにしました(´・ω・｀)")
                    elif "蹴り保護:オフ" == msg.text:
                        if msg.to in wait['pkick']:
                            del wait['pkick'][msg.to]
                            t.sendMessage(msg.to, "蹴り保護をオフにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオフです(´・ω・｀)")
                    elif "URL保護:オン" == msg.text:
                        if msg.to in wait["purl"]:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                        else:
                            G = t.getGroup(msg.to)
                            if G.preventedJoinByTicket == False:
                                G.preventedJoinByTicket = True
                                t.updateGroup(G)
                            wait["purl"][msg.to] = True
                            t.sendMessage(msg.to, "URL保護をオンにしました(´・ω・｀)")
                    elif "URL保護:オフ" == msg.text:
                        if msg.to in wait['purl']:
                            del wait['purl'][msg.to]
                            t.sendMessage(msg.to, "URL保護をオフにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオフです(´・ω・｀)")
                    elif "キャンセル保護:オン" == msg.text:
                        if msg.to in wait["pc"]:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                        else:
                            wait["pc"][msg.to] = True
                            t.sendMessage(msg.to, "キャンセル保護をオンにしました(´・ω・｀)")
                    elif "キャンセル保護:オフ" == msg.text:
                        if msg.to in wait['pc']:
                            del wait['pc'][msg.to]
                            t.sendMessage(msg.to, "キャンセル保護をオフにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオフです(´・ω・｀)")
                    elif "画像保護:オン" == msg.text:
                        if msg.to in wait["pp"]:
                            t.sendMessage(msg.to, "既にオンです(´・ω・｀)")
                        else:
                            wait["pp"][msg.to] = True
                            t.sendMessage(msg.to, "画像保護をオンにしました(´・ω・｀)")
                    elif "画像保護:オフ" == msg.text:
                        if msg.to in wait['pp']:
                            del wait['pp'][msg.to]
                            t.sendMessage(msg.to, "画像保護をオフにしました(´・ω・｀)")
                        else:
                            t.sendMessage(msg.to, "既にオフです(´・ω・｀)")
                    elif "設定確認" == msg.text:
                        group = cl.getGroup(msg.to) 
                        if group.preventedJoinByTicket == False:
                            gu = "オープン"
                        else:
                            gu = "クローズ"
                        if msg.to in wait["pname"]:
                            pn = "オン"
                        else:
                            pn = "オフ"
                        if msg.to in wait["pinv"]:
                            pi = "オン"
                        else:
                            pi = "オフ"
                        if msg.to in wait["pkick"]:
                            pk = "オン"
                        else:
                            pk = "オフ"
                        if msg.to in wait["purl"]:
                            pu = "オン"
                        else:
                            pu = "オフ"
                        if msg.to in wait["pc"]:
                            pc = "オン"
                        else:
                            pc = "オフ"
                        if msg.to in wait["pp"]:
                            pp = "オン"
                        else:
                            pp = "オフ"
                        t.sendMessage(msg.to,"このグル内での設定状況です(´・ω・｀)\n\n☞URL状況:" + gu + "\n☞蹴り保護:" + pk + "\n☞招待保護:" + pi + "\n☞名前保護:" + pn + "\n☞URL保護:" + pu + "\n☞画像保護:" + pp + "\n☞キャンセル保護:" + pc)
                    elif "Negi:解雇" == msg.text:
                        G =cl.getGroup(msg.to)
                        cl.sendMessage(msg.to, "このbotの事が嫌いでも、ねぎえるの事は嫌いにならないでくっちゃい！\n\nお問い合わせ↓\nhttp://line.me/ti/p/%40ubg0555p")
                        cl.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
            if msg._from in vertex:
                if msg.contentType == 0:
                    if '設定:ブラック追加' == msg.text:
                        wait['wblack'][msg.to] = True
                        t.sendMessage(msg.to, '追加する連絡先を送信してね(´・ω・｀)')
                    elif '設定:ブラック削除' == msg.text:
                        wait['dblack'][msg.to] = True
                        t.sendMessage(msg.to, '削除する連絡先を送信してね(´・ω・｀)')
                elif msg.contentType == 13:
                    k = random.choice(bots) 
                    if msg.to in wait['wblack']:
                        if msg.contentMetadata['mid'] in wait['black']:
                            k.sendMessage(msg.to, '既にブラリスです(´・ω・｀)')
                            del wait['wblack'][msg.to]
                        else:
                            wait['black'][msg.contentMetadata['mid']] = True
                            k.sendMessage(msg.to, 'ブラリスに追加しました(´・ω・｀)')
                            del wait['wblack'][msg.to]
                    elif msg.to in wait['dblack']:
                        if msg.contentMetadata['mid'] in wait['black']:
                            del wait['black'][msg.contentMetadata['mid']]
                            k.sendMessage(msg.to, 'ブラリスから削除しました(´・ω・｀)')
                            del wait['dblack'][msg.to]
                        else:
                            k.sendMessage(msg.to, 'ブラリスではありません(´・ω・｀)')
                            del wait['dblack'][msg.to]
                    elif msg.to in wait['mute']:
                        pass
                    else:
                        if msg.contentMetadata['mid'] in wait['black']:
                            k.sendMessage(msg.to, 'ブラリスです(´・ω・｀)')
                        else:
                            k.sendMessage(msg.to, 'ブラリスではないです(´・ω・｀)')

    except Exception as e:
        print (e)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print (e)