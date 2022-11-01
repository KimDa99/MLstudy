## This is place for Learning basic of PyTorch

- [ ] PyTorch Tutorial (https://pytorch.org/tutorials/)
  - [x] Tensors
  - [ ] Datasets and DataLoaders
  - [ ] Transform
  - [ ] Build Model
  - [ ] Automatic Differentiation
  - [ ] Optimization Loop
  - [ ] Save, Load and Use Model
# 컴시구 중간

- CH1: Computer Abstractions and Technology
    - 사용 목적에 맞게 만드는 것이 중요하다. Performance가 좋다고 적절한 것이 아니다.
    - Performance를 결정하는 Parameters
        - 알고리즘 (알고리즘 복잡도)
        - 프로그래밍 언어, 컴파일러
        - processor and memory system
        - I/O system
    - 7 Great Ideas
        - Abstraction
        - make common case fast
        - parrallelism
        - pipelineing
        - prediction
        - Hierarchy
        - Dependability
    - Intergrated Circuit Cost (수율 Yield)
        
        ![Untitled](%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%89%E1%85%B5%E1%84%80%E1%85%AE%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%80%E1%85%A1%E1%86%AB%2038b819dabb9c437284e22b17799a9519/Untitled.png)
        
    - Performance
        - Response time : how long it takes to do a task, Task를 얼마나 빨리 처리하느냐 (ex: 100ms)
        - Throughput : total work per unit time, 해당 시간동안 얼마나 많은 Task를 처리하느냐(ex: tasks per an hour)
    - Relative performance
        - performance = 1/Execution Time
            - ex) X is *k* fater than Y (k = Y.ExeTime / X.ExeTime = X.Performance / Y.Performance)
            - Mesuring Execution Time
                - Elapsed time: total response Time
                    - determines system performance
                - CPU time: time spent processing a given job (excluding I/O time etc.)
                    - consist of user CPU time + system CPU time
                    - CPU Time .. 결국 실제 실행을 시켜봐야 안다.
                        
                        ![Untitled](%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%89%E1%85%B5%E1%84%80%E1%85%AE%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%80%E1%85%A1%E1%86%AB%2038b819dabb9c437284e22b17799a9519/Untitled%201.png)
                        
                        - CPU Time = CPU Clock Cycles * Clock Cycle Time = CPU Clock Cycles / Clock Rate
                            - Performance improved by
                                - number of clock cycles ⬇️
                                - clock rate ⬆️
                                - Hardware에서 clock rate과 cycle count는 trade-off 관계에 놓여있다.
                            - CPU Clocking
                                
                                ![Untitled](%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%89%E1%85%B5%E1%84%80%E1%85%AE%20%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%80%E1%85%A1%E1%86%AB%2038b819dabb9c437284e22b17799a9519/Untitled%202.png)
                                
                                - Clock period: duration of a clock cycle (rising edge ~ rising edge)  ( ex: 250ps = 0.25ns = 250×10^(-12)s )
                                - Clock frequency (rate): cycles per second ( ex: 4.0GHz = 4000MHz = 4.0×10^(9)Hz )
                            - example
