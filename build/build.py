import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import bk as S
import pages_core, pages_guides, pages_tools, pages_ops, pages_legal
pages_core.home(); pages_core.ages(); pages_core.join(); pages_core.about_contact_misc()
pages_guides.build(); pages_tools.build(); pages_ops.build(); pages_legal.build()
S.finish()
