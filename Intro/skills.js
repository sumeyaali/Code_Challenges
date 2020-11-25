// You can see this Input: flightLength movies Output: boolean True 
// if there exists TWO different movies that add up EXACTLY to the flightLength Examples: flightLength 160  Movies [80, 110, 40] => false [80, 110, 80] => true [20, 30, 110, 40, 50] => true

// const movies = [20, 30, 110, 40, 50]


const lengthOfMovie = (movies, flightLength) => {
    // loop through movies array
    const dictionary = {}
    
    for(let i = 0; i > movies.length; i++) {
        let target = flightLength - movies[i]
        if(dictionary[target]){
            return true
        }
        dictionary[movies[i]] = 1
    }
    return false
}