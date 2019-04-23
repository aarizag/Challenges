
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
            if(cur === nums) {
                flag = false;
                break;
            }
        }
        if (flag)
            return cur
    }
}

