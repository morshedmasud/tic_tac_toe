from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import tic_tac
import random
# Create your views here.

# Global Variable
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
human = "X"
computer = "O"



# Viewss
def index(request):

    if request.method == 'POST':
        if request.POST.get('v') == 'reset':
            tic_tac.reset(board)
            messages.info(request, "Board Cleared,, let's play again!!")
        else:
            ###### Human Move #####
            u = int(request.POST.get("v"))
            if tic_tac.legal_spot(u, board):
                board[u] = human
            else:
                messages.warning(request, "This spot already teken!! choose another spot..")
                return redirect('index')

            # Check Human won or not
            if tic_tac.check_wins_line(human, board):
                messages.success(request, "You won the match!! congratulation! wanna play again just click Reset button. ")
                return redirect("index")

            # If no more valid spot
            print("valid spot---- ", tic_tac.valid_spot(board))
            if not tic_tac.valid_spot(board):
                print("no more valdi spot---")
                messages.success(request, "This time you lucky,, Match Tie!! wanna play again just click Reset button.")
                return redirect("index")



            ###### Computer Move #####
            spot = tic_tac.computer_move(board)
            if tic_tac.legal_spot(spot, board):
                board[spot] = computer

                if tic_tac.check_wins_line(computer, board):
                    messages.success(request, "Computer won the match,,  wanna play again just click Reset button.")
                    return redirect("index")
            # while True:
            #     spot = random.randint(0, 8)
            #     print("spot--", spot)
            #     if legal_spot(spot):
            #         board[spot] = computer
            #         break
            # Check Computer won or not

    context = {
        'board': board,
    }
    return render(request, 'index.html', context)