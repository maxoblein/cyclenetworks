function [upgradeEdge,spentBudget]=selectEdgeUpgrade(isEdgeCycle,numEdge,lengthEdge,flowEdge,budget)
%function [upgradeEdge,spentBudget]=selectEdgeUpgrade(isEdgeCycle,lengthEdge,flowEdge,budget)
% order the edges which aren't already upgraded
% In the event of ties on flow, this will allocate according to numerical
% order
inds=[1:numEdge]';
inds=inds(~isEdgeCycle);
flowEdge=flowEdge(~isEdgeCycle);
lengthEdge=lengthEdge(~isEdgeCycle);
[flowEdge,I]=sort(flowEdge,'descend'); inds=inds(I); lengthEdge=lengthEdge(I);
lengthEdgeCumulative = cumsum(lengthEdge);
upgradeEdgeTmp = (lengthEdgeCumulative<budget);
budgetAllocatedTmp = sum(upgradeEdgeTmp.*lengthEdge);
indTmp = sum(upgradeEdgeTmp)+1;  % the edge under consideration.
if (budget-budgetAllocatedTmp)>0.5*lengthEdge(indTmp)
    upgradeEdgeTmp(indTmp)=true;
end
% so the next edge in the list is added if more than half the budget
% required is available.
upgradeEdge=inds(upgradeEdgeTmp);
spentBudget=sum(lengthEdge(upgradeEdgeTmp));
end
