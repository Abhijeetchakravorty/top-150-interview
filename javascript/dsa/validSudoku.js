var isValidSudoku = function (board) {
    const rows = new Array(9).fill().map(() => new Set());
    const cols = new Array(9).fill().map(() => new Set());
    const squares = new Array(3)
        .fill()
        .map(() => new Array(3).fill().map(() => new Set()));

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (board[r][c] === ".") continue;

            if (
                rows[r].has(board[r][c]) ||
                cols[c].has(board[r][c]) ||
                squares[Math.trunc(r / 3)][Math.trunc(c / 3)].has(board[r][c])
            )
                return false;

            rows[r].add(board[r][c]);
            cols[c].add(board[r][c]);
            squares[Math.trunc(r / 3)][Math.trunc(c / 3)].add(board[r][c]);
        }
    }
    return true;
};

console.log(
    isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ])
);
