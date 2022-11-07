//
// Copyright (C) 2007 Peterpaul Klein Haneveld
//
// SPDX-License-Identifier: LGPL-3.0-or-later
//
//

package inet.mobility.single;

import inet.mobility.base.MovingMobilityBase;

//
// Moves a tractor through a field with a certain amount of rows.
// Since the tractor also moves around the field, the tractor travels
// the number of rows PLUS one rows. Consider the following piece of
// ascii-art for rows=2.
//
// <pre>
// >>>>>>>>>>>>>>>v
// ^              v
// ^              v
// <<<<<<<<<<<<<<<<
// v              ^
// v              ^
// >>>>>>>>>>>>>>>^
// </pre>
//
// NOTE: Does not yet support 3-dimensional movement.
// @author Peterpaul Klein Haneveld
//
simple TractorMobility extends MovingMobilityBase
{
    parameters:
        //double speed @unit(mps);
        
        //volatile double angleDelta @unit(deg); // rotate velocity vector by this much around the rotation axis defined by the rotationAxisAngle parameter (can be random)
        //volatile double rotationAxisAngle @unit(deg) = default(0deg); // defines a vector in the plane perpendicular to the velocity, where 0 deg means the Z axis when bank is zero (can be random)
        volatile double speed @mutable @unit(mps); // speed (can be random, updated every changeInterval)
        //volatile double changeInterval @unit(s); // frequency of changing speed and angle (can be random)
        bool initFromDisplayString = default(true);
        //////////////////////////*********change here**********///////////////////////////////////////
        double x1 @unit(m);
        double y1 @unit(m);
        double x2 @unit(m);
        double y2 @unit(m);
        int rowCount; // the number of rows on the field
        @class(TractorMobility);
}

