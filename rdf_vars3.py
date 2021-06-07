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
using rvec_b = const RVec<bool> &;

// this function defines the cuts
float get_CUT(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI, rvec_b PID, float ptMin, float etaMin)
        {
                if (NP > 3)
                {
                  if (PT[3] < ptMin) return -95.;
                  if ((fabs(ETA[0]) > etaMin) or (fabs(ETA[1]) > etaMin) or (fabs(ETA[2]) > etaMin) or (fabs(ETA[3]) > etaMin)) return -90.;
                  if (PID[0]==1 && PID[1]==1 && PID[2]==1 && PID[3]==1) {
                    // passed the cuts
                    return 1.;
                  }
                }
                return -100.;
        }  // get_CUT

// this function gets the pairing by minimizing the dR

float get_min_DRpair(unsigned int NP, rvec_f M, rvec_f PT, rvec_f ETA, rvec_f PHI)
       {

	TLorentzVector v1;
        TLorentzVector v2;
        TLorentzVector v3;
        TLorentzVector v4;
        v1.SetPtEtaPhiM(PT[0],ETA[0],PHI[0],M[0]);
        v2.SetPtEtaPhiM(PT[1],ETA[1],PHI[1],M[1]);
        v3.SetPtEtaPhiM(PT[2],ETA[2],PHI[2],M[2]);
        v4.SetPtEtaPhiM(PT[3],ETA[3],PHI[3],M[3]);

        float DR12 = v1.DeltaR(v2);
        float DR13 = v1.DeltaR(v3);
        float DR14 = v1.DeltaR(v4);
        float DR23 = v2.DeltaR(v3);
        float DR24 = v2.DeltaR(v4);
        float DR34 = v3.DeltaR(v4);
        float DeltaDR1234 = DR12 + DR34;
        float DeltaDR1324 = DR13 + DR24;
        float DeltaDR1423 = DR14 + DR23;

         //      cout << "DeltaDR1234 " << DeltaDR1234 << " DeltaDR1324 "<< DeltaDR1324 << " DeltaDR1423 " << DeltaDR1423 << endl;

        if (min({DeltaDR1234, DeltaDR1324, DeltaDR1423}) == DeltaDR1234) {
           //      cout << "combo 1"  << endl;
          float am1 = (v1+v2).M();
          float am2 = (v3+v4).M();
          float amavg = (am1+am2)/2.;
          return amavg;
         }
        else if (min({DeltaDR1234, DeltaDR1324, DeltaDR1423}) == DeltaDR1324) {
           //      cout << "combo 2" << endl;
          float am1 = (v1+v3).M();
          float am2 = (v2+v4).M();
          float amavg = (am1+am2)/2.;
          return amavg;
         }
        else if (min({DeltaDR1234, DeltaDR1324, DeltaDR1423}) == DeltaDR1423) {
           //      cout << "combo 3" << endl;
          float am1 = (v1+v4).M();
          float am2 = (v2+v3).M();
          float amavg = (am1+am2)/2.;
          return amavg;
         }
        else {
           //      cout << "failed"  <<endl ;
          return -999.; // failed
         }

       } // dR pairing
                                          
