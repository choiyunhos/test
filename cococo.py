# 게시판 만들기

import os
import sys
import time
import pickle
import datetime

# 게시판 클래스
class Board:
    def __init__(self, title, content, writer, date):
        self.title = title
        self.content = content
        self.writer = writer
        self.date = date

    def __str__(self):
        return "제목: " + self.title + "내용: " + self.content + " 작성자: " + self.writer + "  작성일: " + self.date + "   "  
    
# 게시판 리스트
board_list = []

# 게시판 파일
board_file = "board.dat"

# 게시판 파일 로드
def load_board():
    global board_list
    if os.path.exists(board_file):
        with open(board_file, "rb") as f:
            board_list = pickle.load(f)

# 게시판 파일 저장
def save_board():
    with open(board_file, "wb") as f:
        pickle.dump(board_list, f)

# 게시판 메뉴
def board_menu():
    while True:
        print("1. 게시판 글쓰기")
        print("2. 게시판 글보기")
        print("3. 게시판 글수정")
        print("4. 게시판 글삭제")
        print("5. 게시판 종료")
        menu = input("메뉴를 선택하세요: ")
        if menu == "1":
            write_board()
        elif menu == "2":
            read_board()
        elif menu == "3":
            update_board()
        elif menu == "4":
            delete_board()
        elif menu == "5":
            print("게시판을 종료합니다.")
            save_board()
            break
        else:
            print("메뉴를 잘못 선택하셨습니다.")

# 게시판 글쓰기
def write_board():
    title = input("제목을 입력하세요: ")
    content = input("내용을 입력하세요: ")
    writer = input("작성자를 입력하세요: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    board = Board(title, content, writer, date)
    board_list.append(board)
    print("게시판에 글이 등록되었습니다.")

# 게시판 글보기
def read_board():
    for board in board_list:
        print(board)

# 게시판 글수정
def update_board():
    title = input("수정할 제목을 입력하세요: ")
    for board in board_list:
        if board.title == title:
            board.content = input("내용을 입력하세요: ")
            board.writer = input("작성자를 입력하세요: ")
            board.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("게시판 글이 수정되었습니다.")
            return
    print("게시판에 해당 제목이 없습니다.")

# 게시판 글삭제
def delete_board():
    title = input("삭제할 제목을 입력하세요: ")
    for board in board_list:
        if board.title == title:
            board_list.remove(board)
            print("게시판 글이 삭제되었습니다.")
            return
    print("게시판에 해당 제목이 없습니다.")

# 게시판 시작
def board_start():
    load_board()
    board_menu()

if __name__ == "__main__":
    board_start()
