// Kinematic variables for RDF
#include <vector>
#include <stdexcept>
#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>
#include "ROOT/RVec.hxx"

using namespace ROOT::VecOps;
using rvec_f = const RVec<float> &;

float get_XM(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI, float ptMin, float etaMin)
        {
                if (NP > 3)
                {
                                if (PT[3] < ptMin) return -95.;
                                if ((fabs(ETA[0]) > etaMin) or (fabs(ETA[1]) > etaMin) or (fabs(ETA[2]) > etaMin) or (fabs(ETA[3]) > etaMin)) return -90.;
                        ROOT::Math::PtEtaPhiMVector v1(PT[0],ETA[0],PHI[0],M[0]);
                                                ROOT::Math::PtEtaPhiMVector v2(PT[1],ETA[1],PHI[1],M[1]);
                        ROOT::Math::PtEtaPhiMVector v3(PT[2],ETA[2],PHI[2],M[2]);
                                                ROOT::Math::PtEtaPhiMVector v4(PT[3],ETA[3],PHI[3],M[3]);
                                                return (v1+v2+v3+v4).M();
                }
                return -100.;
        }

