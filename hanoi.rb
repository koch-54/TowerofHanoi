def towerofHanoi(n, start, mid, goal)
    if n == 0 then
        return
    end
    towerofHanoi(n - 1, start, goal, mid)
    puts "disk: #{n} start: #{start} goal: #{goal}"
    towerofHanoi(n - 1, mid, start, goal)
end

N = 3
towerofHanoi(N, 'A', 'B', 'C')
