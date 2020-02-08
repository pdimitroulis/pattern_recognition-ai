% GA Optimization
%
% Example
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc;clear;

for runs=1:10
    ObjectiveFunction = @simple_fitness_2;
    nvars = 2;    % Number of variables
    LB = [0 -Inf];   % Lower bound
    UB = [10 10];  % Upper bound
    ConstraintFunction = @simple_constraint_2;

    OPTIONS = gaoptimset('PopulationSize',1000); %original value was 30

    % COSNTRAINED OPTIMIZATION
    [opt_sol,fval] = ga(ObjectiveFunction,nvars,[],[],[],[],LB,UB, ...
        ConstraintFunction)

    %OPTIONS.PopulationSize = 40

    % UNCONTSTRAINED OPTIMIZATION
%     [opt_sol,fval] = ga(ObjectiveFunction,nvars)
end
