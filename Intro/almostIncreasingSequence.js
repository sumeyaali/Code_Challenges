function almostIncreasingSequence(sequence) {
    let deleted = 0
    for (let i = 0; i < sequence.length; i++){
        if (sequence[i] <= sequence[i-1]){
            deleted++
            if (sequence[i] <= sequence[i-2] && sequence[i+1] <= sequence[i-1]){
                return false
            }
        }
    }
    if (deleted > 1){
        return false
    }
    return true
}