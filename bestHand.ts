function bestHand(ranks: number[], suits: string[]): string {
    let suit_counts: Object = {};
    let rank_counts: Object = {};
    for(let i = 0; i<ranks.length;i++) {
        rank_counts[ranks[i]] ? rank_counts[ranks[i]] += 1 : rank_counts[ranks[i]] = 1;
        suit_counts[suits[i]] ? suit_counts[suits[i]] += 1 : suit_counts[suits[i]] = 1;
    }
    console.log(Object.keys(suit_counts).map(key => suit_counts[key]).filter(cnt =>cnt >= 5))
    if(Object.keys(suit_counts).map(key => suit_counts[key]).filter(cnt =>cnt >= 5).length>0) {
        return "Flush"
    }
    if (Object.keys(rank_counts).map(key => rank_counts[key]).filter(cnt => cnt > 2).length>0) {
        return "Three of a Kind"
    }
     if (Object.keys(rank_counts).map(key => rank_counts[key]).filter(cnt => cnt > 1).length>0) {
        return "Pair"
    }
    return "High Card"

};