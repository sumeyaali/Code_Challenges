const buildCalc = () => {

    const [counter, setCounter] = useState(0)

    const onClick = () => {
        setCounter(counter + 1)
    }

    return (
        <div>
            <h1>{counter}</h1>
            <button onClick={onClick}>Increment</button>
        </div>
    )
}


// Problem 2: print an object with the letter as the key and the occurance of that letter as a value

const word = 'jksdofirwsjifdijjarehouvneec'

myCounter = {}

const iterate = () => {

    for(let i = 0; i < word.length; i++) {
        if (myCounter[word[i]]) {
            // if letter is in my dictionary, than increment the value of the leter by 1, else add it to my dictionary
            myCounter[word[i]] = myCounter[word[i]] + 1
        }
        else {
          myCounter[word[i]] = 1
        }
    }
    return myCounter
}

console.log(iterate(word))