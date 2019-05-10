import "./tester"

function* pos_num_generator(x=1){
    while(true){
        yield x;
        x += 1;
    }
}

function non_constant_space(nums){
    let num_set = new Set(nums);
    let pos_nums = pos_num_generator();
    while(true){
        let n = pos_nums.next().value;
        if(!(num_set.has(n)))
            return n
    }
}

function non_linear_time(nums){
    let pos_nums = pos_num_generator();
    let flag;
    while (true){
        let cur = pos_nums.next().value;
        flag = true;
        for(let i = 0; i < nums.length; i++){
            if(cur === nums[i]) {
                flag = false;
                break;
            }
        }
        if (flag)
            return cur
    }
}

function test_lowest_missing(){
    let t1 = [3, 4, -1, 1];
    let t2 = [1, 2, 0];
    let functions = [non_constant_space, non_linear_time];
    let tests = [t1, t2];

    test.test(tests, functions)
}