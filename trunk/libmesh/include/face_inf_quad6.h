// $Id: face_inf_quad6.h,v 1.16 2003-08-18 14:44:52 ddreyer Exp $

// The Next Great Finite Element Library.
// Copyright (C) 2002  Benjamin S. Kirk, John W. Peterson
  
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
  
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
  
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA



#ifndef __inf_quad6_h__
#define __inf_quad6_h__


#include "mesh_config.h"
#ifdef ENABLE_INFINITE_ELEMENTS


// C++ includes


// Local includes
#include "face_inf_quad.h"



/**
 * The \p INFQUAD6 is an infinite element in 2D composed of 6 nodes.
 * It is numbered like this:
   \verbatim
             2     5     3
   INFQUAD6: o     o     o   closer to infinity
             |           |
             |           |
             |           |  
             |           |
             |           |
             o-----o-----o   base side
             0     4     1
   \endverbatim
 */

// ------------------------------------------------------------
// InfQuad6 class definition
class InfQuad6 : public InfQuad
{
public:

  /**
   * Constructor.  By default this element has no parent.
   */
  InfQuad6  (const Elem* p=NULL);
  
  /**
   * @returns 6
   */
  unsigned int n_nodes() const { return 6; }
  
  /**
   * @returns \p INFQUAD6
   */
  ElemType type () const { return INFQUAD6; }
  
  /**
   * @returns 2
   */
  unsigned int n_sub_elem() const { return 2; }
  
  /**
   * @returns \p SECOND
   */
  Order default_order() const { return SECOND; }
  
  /**
   * @returns an \p Edge3 for the base (0) side, and an \InfEdge2 for
   * the sides 1, 2.
   */
  AutoPtr<Elem> build_side (const unsigned int i) const;

  const std::vector<unsigned int> tecplot_connectivity(const unsigned int sf=0) const;
  
  void vtk_connectivity(const unsigned int,
			std::vector<unsigned int>*) const;
  
  unsigned int vtk_element_type (const unsigned int) const
  { return 9; }

  /**
   * @returns 2 for all \p n
   */
  unsigned int n_second_order_adjacent_vertices (const unsigned int) const
      { return 2; }

  /**
   * @returns the element-local number of the  \f$ v^{th} \f$ vertex
   * that defines the \f$ n^{th} \f$ second-order node.
   * Note that \p n is counted as depicted above, \f$ 4 \le n < 6 \f$.
   */
  unsigned short int second_order_adjacent_vertex (const unsigned int n,
						   const unsigned int v) const;
  
  
  
protected:
  
  
#ifdef ENABLE_AMR
  
  /**
   * Matrix used to create the elements children.
   */
  float embedding_matrix (const unsigned int i,
			  const unsigned int j,
			  const unsigned int k) const
  { return _embedding_matrix[i][j][k]; }

  /**
   * Matrix that computes new nodal locations/solution values
   * from current nodes/solution.
   */
  static const float _embedding_matrix[2][6][6];
  
#endif


private:
  
  /**
   * Matrix that tells which vertices define the location
   * of mid-side (or second-order) nodes
   */
  static const unsigned short int _second_order_adjacent_vertices[2][2];
    
};





// ------------------------------------------------------------
// InfQuad6 class member functions
inline
InfQuad6::InfQuad6(const Elem* p) :
  InfQuad(InfQuad6::n_nodes(), p) 
{
}


#endif // ifdef ENABLE_INFINITE_ELEMENTS

#endif
