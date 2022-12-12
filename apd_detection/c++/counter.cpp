#include <iostream>
#include <chrono>

namespace {
    // Define clock type
    typedef std::chrono::high_resolution_clock clock;
}

int main()
{
    // Define real time units
    typedef std::chrono::duration<unsigned long long, std::pico> picoseconds;
    // or:
    // typedef std::chrono::nanoseconds nanoseconds;
    // Define double-based unit of clock tick
    typedef std::chrono::duration<double, typename clock::period> Cycle;
    using std::chrono::duration_cast;
    const int N = 100;
    // Do it
    auto t0 = clock::now();
    for (int j = 0; j < N; ++j)
        asm volatile("");
    auto t1 = clock::now();
    // Get the clock ticks per iteration
    auto ticks_per_iter = Cycle(t1-t0)/N;


    // std::cout << ticks_per_iter.count() << " clock ticks per iteration\n";
    // // Convert to real time units
    // std::cout << duration_cast<picoseconds>(ticks_per_iter).count()
    //           << "ps per iteration\n";
    
    std::cout << duration_cast>picoseconds>

    return 0;
}