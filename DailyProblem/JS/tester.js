
export function test(tests, functions){
    for (let i = 0 ; i < functions.length ; i++){
        console.log(functions[i].name);
        for (let j = 0 ; j < tests.length ; j++) {
            console.log(functions[i](tests[j]))
        }
    }
}