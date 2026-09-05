#!/usr/bin/env python3
import importlib.util
from pathlib import Path
import os
import unittest
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('feedback',Path(__file__).resolve().parents[1]/'scripts/compile_feedback.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class Feedback(unittest.TestCase):
    def test_current_diagnostics_both_hosts(self):
        for cmd_key, out_key in [('command','tool_response'),('cmd','tool_output')]:
            data={'tool_input':{cmd_key:'latexmk -pdf paper.tex'},out_key:{'output':"LaTeX Warning: Reference x undefined.\nOverfull \\hbox (9pt)"}}
            result=module.feedback(data)
            self.assertIn('Compiler diagnostics',str(result))
            self.assertIn('hookSpecificOutput',result)
    def test_no_stale_or_unrelated_reminder(self):
        for command, output in [('cat paper.log','Reference x undefined'),('echo latexmk','Reference x undefined'),('latexmk paper.tex','Output written on paper.pdf'),('python plot.py','done')]:
            self.assertIsNone(module.feedback({'tool_input':{'cmd':command},'tool_output':output}))
    def test_cursor_and_failure(self):
        with patch.dict(os.environ,{'CURSOR_PLUGIN_ROOT':'/tmp/plugin'}):
            result=module.feedback({'tool_input':'cd paper && xelatex main.tex','tool_response':{'stderr':'! Fatal error occurred','exit_code':1}})
            self.assertIn('additional_context',result)
        self.assertIsNone(module.feedback({'tool_input':{'cmd':"latexmk '"}}))

if __name__=='__main__':
    unittest.main()
