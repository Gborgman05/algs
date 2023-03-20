function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    // greedy approach
    let can_place: number = 0;
    for(let i=0;i<flowerbed.length;i++){
        if(!flowerbed[i] && !flowerbed[i-1] && !flowerbed[i+1]) {
            can_place++;
            flowerbed[i] = 1;
        }
    }
    return can_place >= n;

};