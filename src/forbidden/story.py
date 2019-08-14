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
    return w.scene("私の仕事",
            # NOTE: 代替臓器製造研究
            # NOTE: 研究所、知的生命体を合成する、失敗ばかり
            )

def sc_chattime(w: wd.World):
    m = doc = w.doc
    h = eri = w.eri
    return w.scene("おしゃべりの時間",
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

