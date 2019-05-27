# -*- coding: utf-8 -*-
"""Chapter 05: the red-chain
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.redchain import config as cnf
THM = cnf.THEMES


# scenes
def sc_gobacktown(w: wd.World):
    ma = w.masuda
    return w.scene("帰郷",
            ma.be(w.stage.train, "新幹線"),
            ma.think("今回の調査について"),
            ma.look("杉岡からの連絡"),
            )

def sc_sugiokatalk(w: wd.World):
    ma, sugi = w.masuda, w.sugioka
    return w.scene("杉岡の話",
            ma.come(w.stage.bar),
            ma.talk(w.sugioka, w.hideko),
            ma.deal("自分の仕入れた話"),
            sugi.talk("よくそこまで調べたな"),
            ma.hear(sugi, "彼の調査"),
            ma.think("結局杉岡の方が調べていた"),
            sugi.talk("彼女の男の話"),
            ma.know("付き合っていたのは別の学生時代からの男"),
            ma.ask("今どこに？"),
            sugi.talk("埼玉の墓の下"),
            sugi.talk("会社は辞めてフリーになる"),
            sugi.talk("秀子に関わったからかな"),
            )

def sc_ceasechain(w: wd.World):
    ma, tanabe, miki = w.masuda, w.tanabe, w.miki
    return w.scene("途絶えた繋がり",
            ma.come(w.stage.office),
            w.tag.comment("これまでの簡単なまとめと足取りが途絶えたこと。付き合っていたらしい男は二十年前に病死"),
            ma.talk(tanabe, "諸々"),
            miki.talk("ひっそり発表"),
            ma.look("web記事"),
            ma.know("本名"),
            ma.think("同じ苗字"),
            ma.ask(tanabe, "無縁仏の行方"),
            )

def sc_townofficer(w: wd.World):
    ma, hino = w.masuda, w.hino
    return w.scene("役所の対応",
            ma.come(w.stage.townoffice),
            # NOTE: 対応は「市民課」等
            ma.meet(w.hino),
            ma.hear(w.hino, w.i.deal_deads),
            hino.talk("無縁仏の扱い"),
            ma.ask("秀子は？"),
            )

def sc_unrelated(w: wd.World):
    ma, priest = w.masuda, w.priest
    return w.scene("無縁仏",
            ma.go(w.stage.temple),
            ma.talk(w.priest),
            w.priest.talk("無縁仏の処理"),
            ma.hear(w.priest, w.i.deal_deads),
            w.priest.talk("この前の火災の"),
            # NOTE: 祥子は遺骨を受け取らず、ここに収めてと頼む
            ma.know(w.doc),
            )

def sc_inquest(w: wd.World):
    ma, doc = w.masuda, w.doc
    return w.scene("検死結果",
            ma.come(w.stage.medicals, w.day.interview3),
            ma.know(w.doc),
            ma.meet(w.doc),
            ma.talk(w.doc, w.i.doc_secret),
            doc.talk("遺体について"),
            ma.hear(w.doc, w.deadbody),
            doc.talk("あれは臍の緒だった"),
            ma.know(w.anotherbody, w.benio),
            ma.know(w.i.truth),
            ma.think(cnf.THEMES["chain"]),
            )

def sc_thesite(w: wd.World):
    ma, takamori = w.masuda, w.takamori
    return w.scene("火災現場",
            ma.come(w.stage.thesite),
            ma.look("再度調査"),
            ma.meet(takamori),
            takamori.talk("ずっと空き家だったが誰か住んでた"),
            takamori.talk("幽霊の話があってな"),
            )

# episodes
def ep_truth(w: wd.World):
    return [w.chaptertitle("彼女の真実"),
            sc_gobacktown(w),
            sc_sugiokatalk(w),
            sc_townofficer(w),
            sc_unrelated(w),
            sc_inquest(w),
            sc_thesite(w),
            ]

# main
def story(w: wd.World):
    return ep_truth(w)


def main(): # pragma: no cover
    from src.redchain.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

