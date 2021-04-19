%% set-up
clear; close all; more off
%beta=1.35; numNode=20;
beta=1.45; numNode=30;
omega=2;
lambda=inf; %shortest paths only
ODmatrix=ones(2,2);
% * numNode=10, beta=1.0 - very stripped down networks - moving only just
% beyond cross -  the majority are just 10,11 edges - NDP could be run.
% * numNode=20, beta=1.3, or beta=1.4 - NB NDP is not possible, as number
% of edges typically up at 24+..., 1.35 might be the happy compromise.
numIter=100; % size of ensemble
for i=1:numIter
[ALLlistEdge{i},ALLlengthEdge{i},ALLnumEdge(i),ALLx{i},ALLy{i},...
    ALLOnode{i},ALLDnode{i},ALLG{i},ALLnodePath{i},ALLedgePath{i}] = makeNetwork(numNode,beta);
end
figure; hist(ALLnumEdge,[1:50]);
%% Plot what random samples look like
figure; 
i = randi(numIter);
plot(ALLx{i}(ALLlistEdge{i})',ALLy{i}(ALLlistEdge{i})','r-')
axis equal
axis([-0.1 1.1 -0.1 1.1])
%% Loop over the networks - extract each network in turn
for i=1:numIter
    listEdge=ALLlistEdge{i}; lengthEdge=ALLlengthEdge{i}; numEdge=ALLnumEdge(i);
    x=ALLx{i}; y=ALLy{i}; Onode=ALLOnode{i}; Dnode=ALLDnode{i}; G=ALLG{i}; 
    nodePath=ALLnodePath{i}; edgePath=ALLedgePath{i};
%% Compute the lengths of all the paths in the base network
    isEdgeCycle0 = false(numEdge,1);
    lengthPath0=computePathLength(edgePath,isEdgeCycle0,lengthEdge,omega);
%% Allocate traffic to the base network and compute metrics
% lambda=inf means shortest routes, otherwise SUE with param bet
    [flowEdge0,flowPath0] = allocateTraffic(ODmatrix,lengthPath0,lambda,numEdge,edgePath);
    [cycleProportionFlowWeighted0(i),effectiveLengthFlowWeighted0(i)]=...
    computeMetrics(ODmatrix,flowPath0,edgePath,isEdgeCycle0,lengthEdge,omega);
%% Upgrade 50% of the network in one fell swoop
    budget=0.5*sum(lengthEdge);
    [upgradeEdge,budgetAllocated1(i)]=selectEdgeUpgrade(isEdgeCycle0,numEdge,lengthEdge,flowEdge0,budget);
    isEdgeCycle1 = false(numEdge,1);
    isEdgeCycle1(upgradeEdge)=true;
    lengthPath1=computePathLength(edgePath,isEdgeCycle1,lengthEdge,omega);
    % path lengths also need updating
    [flowEdge1,flowPath1] = allocateTraffic(ODmatrix,lengthPath1,lambda,numEdge,edgePath);
    [cycleProportionFlowWeighted1(i),effectiveLengthFlowWeighted1(i)]=...
    computeMetrics(ODmatrix,flowPath1,edgePath,isEdgeCycle1,lengthEdge,omega);
%% Now instead upgrade in two 25% hits
    budget=0.25*sum(lengthEdge);
    [upgradeEdge,budgetAllocated2a(i)]=selectEdgeUpgrade(isEdgeCycle0,numEdge,lengthEdge,flowEdge0,budget);
    isEdgeCycle2a = false(numEdge,1);
    isEdgeCycle2a(upgradeEdge)=true;
    lengthPath2a=computePathLength(edgePath,isEdgeCycle2a,lengthEdge,omega);
    [flowEdge2a,flowPath2a] = allocateTraffic(ODmatrix,lengthPath2a,lambda,numEdge,edgePath);
    [cycleProportionFlowWeighted2a(i),effectiveLengthFlowWeighted2a(i)]=...
    computeMetrics(ODmatrix,flowPath2a,edgePath,isEdgeCycle2a,lengthEdge,omega);
    budget=0.5*sum(lengthEdge)-budgetAllocated2a(i);
    [upgradeEdge,budgetAllocated2b(i)]=selectEdgeUpgrade(isEdgeCycle2a,numEdge,lengthEdge,flowEdge2a,budget);
    isEdgeCycle2b=isEdgeCycle2a;
    isEdgeCycle2b(upgradeEdge)=true;
    lengthPath2b=computePathLength(edgePath,isEdgeCycle2b,lengthEdge,omega);
    [flowEdge2b,flowPath2b] = allocateTraffic(ODmatrix,lengthPath2b,lambda,numEdge,edgePath);
    [cycleProportionFlowWeighted2b(i),effectiveLengthFlowWeighted2b(i)]=...
    computeMetrics(ODmatrix,flowPath2b,edgePath,isEdgeCycle2b,lengthEdge,omega);
%% Four 12.5% hits
% to be implemented
end
%%
% should use one omega, lambda for upgrading the network, and other
% lambda and omega for measuring the network?
mean(cycleProportionFlowWeighted1)/4
mean(cycleProportionFlowWeighted2b)/4
