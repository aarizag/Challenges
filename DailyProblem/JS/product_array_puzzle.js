
function optimized_prod(nums){
    let x = 1;
    let prod = [];
    for(var i = 0; i < nums.length; i++){
        prod.push(nums[i]);
        x *= nums[i]
    }
    x = 1;
    for(i -= 1 ; i >= 0; i--){
        prod[i] *= x;
        x *= nums[i]
    }
    return prod
}


function with_division(nums){
    function product(x){
        let mul = 1;
        for (let i = 0; i < x.length ; i++)
            mul *= x[i];
        return mul;
    }
    let prod = product(nums);
    let result = [];
    for (let i = 0; i < nums.length; i++)
        result.push(prod/nums[i]);
    return result;
}


function brute_force(nums) {
    let result = [];
    for (let i = 0; i < nums.length; i++){
        let sum = 1;
        for (let j = 0; j < nums.length; j++){
            if (j !== i)
                sum *= nums[j];
        }
        result.push(sum);
    }
    return result;
}



let test1 = [1, 2, 3, 4, 5];
let test2 = [5, 3, 6, 1];
let test3 = [2, 4, 6, 8];
let test4 = [3];

let tests = [test1, test2, test3, test4];

for (let i = 0; i< 4; i++){
    console.log(brute_force(tests[i]));
}