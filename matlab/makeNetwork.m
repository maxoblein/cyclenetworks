function [listEdge,lengthEdge,numEdge,x,y,Onode,Dnode,G,nodePath,edgePath] = makeNetwork(numNode,beta)
%function [listEdge,lengthEdge,numEdge,x,y,Onode,Dnode,G,nodePath,edgePath] = makeNetwork(numNode,beta)
%% Position the nodes
x = sort(0.1 + 0.8*rand(numNode-4,1)); y = 0.1 + 0.8*rand(numNode-4,1);
% interior nodes well inside the unit square, sorted by x for tidiness
x = [[0;0]; x; [1;1]];
y = [[0;1]; y; [0;1]];
% add on origins and destinations
Onode = [1;2];
Dnode = [numNode-1; numNode];
% label the origins and destinations
%% Compute a (cleaned-up) Delaunay triangulation - 
DT=delaunayTriangulation(x,y);
st=DT.edges;
% NB routine auto orders these s,t pairs so that s<t
tmp=[((st(:,1)<3)|(st(:,1)>numNode-2)),(st(:,2)<3)|(st(:,2)>numNode-2)];
inds = find(prod(tmp')');
st(inds,:)=[];
numEdge=size(st,1);
% Remove the edges which correspond to short cuts across sides of box
%% Compute the beta skeleton - adapted from Alonso code
listEdges = st;
edgeVectors = [x(listEdges(:,2))-x(listEdges(:,1)) y(listEdges(:,2))-y(listEdges(:,1))];
edgeLengths = sqrt(sum(edgeVectors.*edgeVectors,2));
edgeUnitVectors = [edgeVectors(:,1)./edgeLengths edgeVectors(:,2)./edgeLengths];
% preparing constructions used by Alonso code
edgeRadii = 0.5*beta*edgeLengths;
C1 = [x(listEdges(:,1))+edgeRadii.*edgeUnitVectors(:,1) y(listEdges(:,1))+edgeRadii.*edgeUnitVectors(:,2)];
C2 = [x(listEdges(:,2))-edgeRadii.*edgeUnitVectors(:,1) y(listEdges(:,2))-edgeRadii.*edgeUnitVectors(:,2)];
% preparing the lunes
numPotentialEdges = length(edgeRadii);
numPoints = length(x);
includeEdge = false(numPotentialEdges,1);
edgeRadii2 = edgeRadii.*edgeRadii;
listPoints = [1:numPoints]';
for i=1:length(edgeRadii)
    test1 = ((x-C1(i,1)).^2 + (y-C1(i,2)).^2)<edgeRadii2(i);
    test2 = ((x-C2(i,1)).^2 + (y-C2(i,2)).^2)<edgeRadii2(i);
    isPoint12 = (listPoints==listEdges(i,1))|(listPoints==listEdges(i,2)); % this is expensive
    includeEdge(i) = sum(test1&test2&~isPoint12)==0;
end
% computes includeEdge - which says which edges should remain in graph
%% Mating Alonso's output back to Max's structures
st = st(includeEdge,:);
numEdge = size(st,1);
lengthEdge = sqrt(diff(x(st)')'.^2+diff(y(st)')'.^2);
listEdge = st;
%% Build Matlab graph structure, and also compute path lists
G=graph(listEdge(:,1),listEdge(:,2));
for i=1:length(Onode)
    for j=1:length(Dnode)
        [nodePath{i,j},edgePath{i,j}]=allpaths(G,Onode(i),Dnode(j));
    end
end
%%
end
% NB unfortunate how the variable name style clashes between Alonso and
% the original code flow.
