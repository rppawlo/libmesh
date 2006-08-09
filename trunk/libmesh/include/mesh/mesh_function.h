// $Id: mesh_function.h,v 1.7 2006-08-09 13:51:48 roystgnr Exp $

// The libMesh Finite Element Library.
// Copyright (C) 2002-2005  Benjamin S. Kirk, John W. Peterson
  
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



#ifndef __mesh_function_h__
#define __mesh_function_h__

// C++ includes
#include <vector>


// Local Includes
#include "function_base.h"
#include "dense_vector.h"



// Forward Declarations
template <typename T> class DenseVector;
class EquationSystems;
template <typename T> class NumericVector;
class DofMap;
class PointLocatorBase;



/**
 * This class provides function-like objects for data
 * distributed over a mesh.  
 *
 * @author Daniel Dreyer, 2003
 */

// ------------------------------------------------------------
// MeshFunction class definition
class MeshFunction : public FunctionBase
{
public:

  /**
   * Constructor for mesh based functions with vectors
   * as return value.  Optionally takes a master function.
   */
  MeshFunction (const EquationSystems& eqn_systems,
		const NumericVector<Number>& vec,
		const DofMap& dof_map,
		const std::vector<unsigned int>& vars,
		const FunctionBase* master=NULL);

  /**
   * Constructor for mesh based functions with a number
   * as return value.  Optionally takes a master function.
   */
  MeshFunction (const EquationSystems& eqn_systems,
		const NumericVector<Number>& vec,
		const DofMap& dof_map,
		const unsigned int var,
		const FunctionBase* master=NULL);

  /**
   * Destructor.
   */
  ~MeshFunction ();



  /**
   * The actual initialization process.
   */
  void init ();

  /**
   * Clears the function.
   */
  void clear ();

  /**
   * @returns the \f$ 0^{th} \f$ entry of the \p std::vector<Number> at point
   * \p p and for \p time, which defaults to zero.  Creates a
   * \p DenseVector<Number> as input to the user-provided method, 
   * so it may be worth thinking about using \p evaluate().
   */
  Number operator() (const Point& p, 
		     const Real time=0.);

  /**
   * Computes values at coordinate \p p and for time \p time, defaults
   * to zero.  It is up to the user-provided method \p _analytical_fptr
   * whether \p output has to have the correct length or should be
   * resized.
   */
  void operator() (const Point& p,
		   const Real time,
		   DenseVector<Number>& output);

  /**
   * Returns the current \p PointLocator object, for you might want to
   * use it elsewhere.  The \p MeshFunction object must be initialized
   * before.
   */
  const PointLocatorBase& get_point_locator (void) const;

  /**
   * Enables out-of-mesh mode.  In this mode, if asked for a point
   * that is not contained in any element, the \p MeshFunction will
   * return the given \p value instead of crashing.  This mode is off
   * per default.  If you use a master mesh function and you want to
   * enable this mode, you will have to enable it for the master mesh
   * function as well and for all mesh functions that have the same
   * master mesh function.  You may, however, specify different
   * values.
   */
  void enable_out_of_mesh_mode(const DenseVector<Number>& value);

  /**
   * Enables out-of-mesh mode.  In this mode, if asked for a point
   * that is not contained in any element, the \p MeshFunction will
   * return the given \p value instead of crashing.  This mode is off
   * per default.  If you use a master mesh function and you want to
   * enable this mode, you will have to enable it for the master mesh
   * function as well and for all mesh functions that have the same
   * master mesh function.  You may, however, specify different
   * values.
   */
  void enable_out_of_mesh_mode(const Number& value);

  /**
   * Disables out-of-mesh mode.  This is also the default.
   */
  void disable_out_of_mesh_mode(void);

protected:


  /**
   * The equation systems handler, from which
   * the data are gathered.
   */
  const EquationSystems& _eqn_systems;

  /**
   * A reference to the vector that holds the data
   * that is to be interpolated.
   */
  const NumericVector<Number>& _vector;

  /**
   * Need access to the \p DofMap of the other system.
   */
  const DofMap& _dof_map;

  /**
   * The indices of the variables within the other system 
   * for which data are to be gathered.
   */
  const std::vector<unsigned int> _system_vars;

  /**
   * A point locator is needed to locate the
   * points in the mesh.
   */
  PointLocatorBase* _point_locator;

  /**
   * \p true if out-of-mesh mode is enabled.  See \p
   * enable_out_of_mesh_mode() for more details.  Default is \p false.
   */
  bool _out_of_mesh_mode;

  /**
   * Value to return outside the mesh if out-of-mesh mode is enabled.
   * See \p enable_out_of_mesh_mode() for more details.
   */
  DenseVector<Number> _out_of_mesh_value;
};




// ------------------------------------------------------------
// MeshFunction inline methods



#endif

