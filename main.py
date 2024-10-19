# ------------------------------------------------------------
# Copyright (c) 2024 C1ph3rPhr3ak. All rights reserved.

# Permission is granted to view, download, and use this software from this repository, provided that:
# - The software is not redistributed in any form.
# - Modifications may only be made through pull requests or issues in this repository.
# - No commercial use of the software is allowed without explicit written consent from the author.

# The software is provided "AS IS," without warranty of any kind.  In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

# This software is strictly intended to be used in an ethical and LEGAL manner ONLY! The authors and copyright holders are NOT liable for any arrest, investigation, or other legal action due to the misuse or abuse of this software.
# -------------------------------------------------------------

import sys
from PyQt5.QtWidgets import QApplication
from gui import MainWindow

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
