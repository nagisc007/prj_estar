# -*- coding: utf-8 -*-
"""Story: The forbidden love
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.forbidden import config as cnf
THM = cnf.THEMES


# scenes
def sc_teatime(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("先生のティータイム",
            m.be(w.stage.myhome, w.day.image),
            m.think("愛はどんな形をしているのか",
                "ということについて何時間も君と話し合ったことを忘れていない"),
            m.think("そもそも愛というのは人間が創造した概念であり",
                "$meはそれが人間に必要なものだから大昔の誰かがこの気持ちを愛と名付けたんだという君の主張に",
                "ナンセンスだとつい激昂してしまったことを思い出すよ"),
            m.think("あの頃まだ$meは",
                "いや$meたちは",
                "愛とはどんな形をしていてどのような味わいなのか",
                "またそれがどんな作用を及ぼし$meたちを変容させていくものなのか",
                "全く分かっていなかったね"),
            m.think("でもね",
                "$meは今$meらの関係がこうなってみて思うんだ。",
                "愛というのは気づかないだけで",
                "本当は常に$meと君の間に横たわっていた見えない絆だったんだと"),
            m.deal("男は白いゴム手袋をしたままで紅茶のティーカップに手を伸ばす"),
            m.look("細い線で描かれた花柄はカップをささやかに彩り",
                "そこに入れられた赤い液体を芳しく感じさせる効果があるようにも思えた"),
            m.deal("液体を僅かに口に含むと",
                "男は微笑を作ろうと口角を上げたが",
                "僅かに開いた唇の端から赤い液体がつう", "と溢れてしまう"),
            m.talk("すまないね。",
                "君の前ではいつも自然と粗相をしてしまう。",
                "だから$meにはいつまでも君がいなくてはいけない。",
                "そのことを君は今もちゃんと理解してくれているだろうか。",
                "ねえ$mirei"),
            m.deal("男はナプキンで口元を拭い",
                "車椅子に掛けている女性に改めて微笑を向けた"),
            m.talk("ああ、そうだね。",
                "もうすぐあの夏がやってくる"),
            m.look("見上げた空には入道雲になろうと精一杯に天へと腕を伸ばす白い塊が",
                "青を突き破っていた"),
            )

def sc_mywork(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    momo, nabe = w.momoko, w.nabe
    return w.scene("私の仕事",
            h.be(w.stage.labo, w.day.current),
            h.deal("真っ白な部屋で無菌エプロンと白いマスクを着け",
                "半透明のゴム手袋を嵌めて", "$n_eriは赤ランプの下で待機をする"),
            momo.talk("毎日毎日洗浄されていると", "そのうち自分が溶けて無くなっちゃうんじゃないかって気になってくるわ"),
            eri.talk("$momokoおはようございます"),
            h.deal("$Sより少しだけ背が高い", "同じ格好をした$n_momokoが眼鏡の上からゴーグルを着けながら「そう思わない？」と視線を向けた"),
            eri.talk("けど$meたちの研究ではいくら人が普段生活するのに細菌との共存が必要だからといってそれらを持ち込むのは厳禁ですから"),
            momo.talk("真面目ねえ。",
                "$meなんかは時々バイオハザードされて製造中の代替臓器がみんな曝露されてしまえって思うこともあるのに"),
            eri.talk("$momokoは過激派です。",
                "いくらお休みが取れないからといって$meはそういう思考はしません。",
                "それに彼らだって生きてるんですよ？",
                "肺や腸や肝臓といったフルサイズばかりでなく", "皮膚や血管といった部品ですらちゃんと生命体なんです"),
            h.hear("ブザーが鳴り", "滅菌ガスのアナウンスが入ると",
                "二人とも目を閉じて軽く腕を上げる"),
            h.deal("白く着色したガスが霧のように上下左右から噴き出して", "二人を包み込んだ"),
            momo.talk("たぶん$eriみたいな生真面目さを", "$doc先生は愛しているんだろうね"),
            eri.talk("な", "なんでここで$docの話になるんですか！"),
            h.deal("$Sは彼女の不意打ちにマスクの中で思い切り咳き込んだが",
                "$fn_momokoの方は何とも思っていないようだ"),
            momo.talk("みんな気づいてないと思ってるの？",
                "二十七歳っていう最年少で$ln_doc教授の研究チーム入りできたのだって", "誰もが先生のお気に入りだからだろうって言ってるわよ"),
            h.feel("お気に入りという言葉に急激な体温上昇を感じた$Sだったが",
                "首を左右に振って否定すると",
                "滅菌終了のアナウンスを確認して隣室へのドアを開けた"),
            eri.talk("$docはちゃんと奥さんがいますから"),
            h.move("きっぱりと口にしてラボに入って行った"),
            w.tag.symbol("◆"),
            h.look("ラボと呼ばれているが", "正式名称は『$st_labo』の『$st_mainroom』だ"),
            h.look("常駐している研究員が二人いて",
                "培養中の代替臓器の監視を二十四時間体制で行っている。",
                "他にも多い時には全部で二十人くらいが研究室には入るが",
                "あまり人が多いと室温が上がり易いということから十人程度までに制限されることが多い"),
            h.look("$Sと$fn_momokoは日中の勤務が主で",
                "$fn_momokoの方は分析を", "$Sはこのラボのチーフであり事実上の研究所のトップでもある$n_docのメイン助手の一人という立場で",
                "代替臓器の研究に従事していた"),
            nabe.talk("よう", "$momokoに$eri"),
            eri.talk("おはようございます"),
            h.deal("沢山並ぶモニタをチェックしていた$n_nabeが入ってきた二人に気づいて声を掛けた。",
                "サブチーフという立場だったが", "培養カプセルの中で育つ人工臓器の成長を見守るのが何より好きだという",
                "根っからの臓器フェチで", "今日で研究所に泊まり込んで何日目になるのだろう",
                "と考えさせられるマスクの上から覗く無精髭の濃さだ。", "その下を想像すると$Sは愛想笑いを浮かべるのが精一杯になる"),
            h.look("がっしりとした体型で身長も百八十くらいある。",
                "仕事のない時はジムに通っているらしいが", "そもそもラボで顔を見ない日がなかった"),
            momo.talk("$docはまだですか？"),
            h.deal("$fn_momokoは分析機器の確認をしながら彼に話し掛ける。",
                "引き継ぎの際に特に何も云われてなかったと$Sは思ったが", "電源のオンオフから一つ一つの器具の汚れまでチェックする姿勢に",
                "仕事に対しての繊細さを感じずにはいられない"),
            nabe.talk("なんか緊急会議が入ったとかで遅れるとは聞いた"),
            eri.talk("緊急ですか？"),
            h.deal("$Sもそれぞれの培養カプセルの数値を記入して歩きながら$ln_nabeに顔を向ける"),
            nabe.talk("$docの奴", "最近何かとオーナー陣と揉めてるって言ってたから",
                    "ひょっとしたらその件かもな"),
            h.think("この$st_laboは一応公的資金の援助を受けているが民間の研究機関だ。",
                    "特に最近は大手外資系ネット企業がスポンサーについたことでちょっとした話題にもなった",
                    "ということは普段ニュースを見ない$Sでも知っていた"),
            momo.talk("じゃあ$docの首が飛んだら次は$nabeが実質代表ですか？"),
            h.look("相変わらずズケズケと訊くな", "と思って$momokoを見やったが",
                    "$ln_nabeは即答でそれを否定する"),
            nabe.talk("あいつがいなくなったら代替臓器研究なんてまともにできるはずないんだから",
                    "$meも一緒に辞めるよ。", "そもそも$meをここに誘ったのも$docだしな"),
            h.deal("$ln_docと$ln_nabeは大学院の同期で$ln_nabeの方が一つだけ年下だそうだ。",
                    "何か事情があって$ln_docは大学を一年休学しているらしい"),
            h.think("$Sも多少の話は聞いていたが", "直接問いかけたことはなく",
                    "いつも$fn_momokoと$ln_nabeたちのやり取りの中で知ることになるのだ"),
            nabe.talk("ああ、それより$eri。",
                    "昨日お前が見てた試験体だけどな", "やっぱり生育不良らしい。",
                    "データは出てるから後で$st_canfroomに戻ってから見といて"),
            eri.talk("え？", "心臓だけですか？", "それとも他の臓器も？"),
            h.deal("今までのものと比べて途中からサイズが大きくならなかったから懸念していたが",
                    "$Sは自分の調整が悪かったのだろうかと肩を落とす"),
            nabe.talk("全てだ。",
                    "ただ$eriの管理が悪かったとかそういうことじゃなくて",
                    "また例の$i_AGEだったよ。", "$meも今朝聞いたばかりなんだが"),
            eri.talk("$i_AGEですか……"),
            h.deal("マスクの中に小さな溜息を落とした時だった。",
                    "ドアが開き", "マスクをしていてもそれとよく分かる通る声で$n_docが挨拶をした"),
            doc.talk("遅れてすまない。", "進捗はどうだい", "$eri"),
            )

def sc_chattime(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("おしゃべりの時間",
            h.be(w.stage.cafe),
            # NOTE: 先生についての噂
            )

def sc_docmind(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("先生の気持ち",
            # NOTE: 二人きり、奥さんをずっと愛している、もう亡くなっているのに、まるで生きているみたい
            )

def sc_dochouse(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("博士のお手伝い",
            # NOTE: 家に招待される
            )

def sc_docwife(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("奥様",
            )

def sc_aftertalk(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("後日談",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("導入部"),
            sc_teatime(w),
            )

def ep_docwife(w: wd.World):
    return (w.chaptertitle("先生の奥様"),
            sc_mywork(w),
            sc_chattime(w),
            sc_docmind(w),
            )

def ep_doll(w: wd.World):
    return (w.chaptertitle("ヒトの形をしたもの"),
            )

def ep_distress(w: wd.World):
    return (w.chaptertitle("苦悩"),
            )

def ep_truth(w: wd.World):
    return (w.chaptertitle("真実"),
            sc_dochouse(w),
            sc_docwife(w),
            sc_aftertalk(w),
            )

# outline
def story_baseinfos(w: wd.World):
    return [
            ]

def story_outlines(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The forbidden love")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("ヒトの形をした愛"),
            ep_intro(w),
            ep_docwife(w),
            ep_doll(w),
            ep_distress(w),
            ep_truth(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

