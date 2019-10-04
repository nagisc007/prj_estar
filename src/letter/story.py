# -*- coding: utf-8 -*-
"""Story: the letter
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.letter import config as cnf
THM = cnf.THEMES


# scenes
# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            # NOTE: つつましい、幸せな日々。手紙を書くのが好きな彼女、ペンを落とす
            )

def ep_hersick(w: wd.World):
    return (w.chaptertitle("彼女の病気"),
            # NOTE: 病気が判明。筋肉系の病気。卵子の保存措置など準備を始める
            )

def ep_modeling(w: wd.World):
    return (w.chaptertitle("彼女をモデルに"),
            # NOTE: 彼女の実際の手をモデル化して造形。彼女の手書き文字を再現する
            )

def ep_herletter(w: wd.World):
    return (w.chaptertitle("彼女からの手紙"),
            # NOTE: 彼女からまだ見ぬ子への手紙。そして試験管で生まれ、人工子宮にて育った子
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
    w = wd.World("The letter")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("彼女はそれでも手紙を書きたかった"),
            ep_intro(w),
            ep_hersick(w),
            ep_modeling(w),
            ep_herletter(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

