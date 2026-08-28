from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol, cast

import numpy as np

if TYPE_CHECKING:
    from networkx import Graph


class _SupportsAddMul(Protocol):
    def __add__(self, *args, **kwargs) -> Any: ...

    def __radd__(self, *args, **kwargs) -> Any: ...

    def __mul__(self, *args, **kwargs) -> Any: ...

    def __rmul__(self, *args, **kwargs) -> Any: ...


def harmony(graph: Graph) -> np.float64:
    """Compute the harmony H (optimization objective) of the given graph.

    H = ∑_i ∑_j [w_aij * a_i * (a_j + w_vj * v_j) + w_vij * v_i * (v_j + w_aj * a_j)]

    Returns:
        float: Current harmony value H.
    """
    H = np.float64(0)

    # Add harmony for all edges.
    for i, j, edge_attr in graph.edges(data=True):
        node_i: dict[str, np.float64] = graph.nodes[i]
        node_j: dict[str, np.float64] = graph.nodes[j]

        H += harmony_term(
            a_i=node_i['a'],
            a_j=node_j['a'],
            v_i=node_i['v'],
            v_j=node_j['v'],
            w_aj=node_j['w_a'],
            w_vj=node_j['w_v'],
            w_aij=edge_attr['w_a'],
            w_vij=edge_attr['w_v'],
        )
        H += harmony_term(
            a_i=node_j['a'],
            a_j=node_i['a'],
            v_i=node_j['v'],
            v_j=node_i['v'],
            w_aj=node_i['w_a'],
            w_vj=node_i['w_v'],
            w_aij=edge_attr['w_a'],
            w_vij=edge_attr['w_v'],
        )

    # Add harmony for all inherent valences.
    for _, data in graph.nodes(data=True):
        if data['w_inherent_valence'] == 0:
            continue

        H += harmony_term(
            a_i=0,
            a_j=data['a'],
            v_i=1,
            v_j=data['v'],
            w_aj=data['w_a'],
            w_vj=data['w_v'],
            w_aij=0,
            w_vij=data['w_inherent_valence'],
        )
        H += harmony_term(
            a_i=data['a'],
            a_j=0,
            v_i=data['v'],
            v_j=1,
            w_aj=0,
            w_vj=0,
            w_aij=0,
            w_vij=data['w_inherent_valence'],
        )

    return cast('np.float64', H)


def harmony_term(
    a_i: _SupportsAddMul,
    a_j: _SupportsAddMul,
    v_i: _SupportsAddMul,
    v_j: _SupportsAddMul,
    w_aj: _SupportsAddMul,
    w_vj: _SupportsAddMul,
    w_aij: _SupportsAddMul,
    w_vij: _SupportsAddMul,
) -> _SupportsAddMul:
    """Calculate one term in the sum of the harmony."""
    return w_aij * a_i * (a_j + w_vj * v_j) + w_vij * v_i * (v_j + w_aj * a_j)
