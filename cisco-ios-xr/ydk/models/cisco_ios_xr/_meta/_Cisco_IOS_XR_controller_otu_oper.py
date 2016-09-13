


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'OtuStateEtEnum' : _MetaInfoEnum('OtuStateEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'not-ready':'NOT_READY',
            'admin-down':'ADMIN_DOWN',
            'down':'DOWN',
            'up':'UP',
            'shutdown':'SHUTDOWN',
            'error-disable':'ERROR_DISABLE',
            'down-immediate':'DOWN_IMMEDIATE',
            'down-immediate-admin':'DOWN_IMMEDIATE_ADMIN',
            'down-graceful':'DOWN_GRACEFUL',
            'begin-shutdown':'BEGIN_SHUTDOWN',
            'end-shutdown':'END_SHUTDOWN',
            'begin-error-disable':'BEGIN_ERROR_DISABLE',
            'end-error-disable':'END_ERROR_DISABLE',
            'begin-down-graceful':'BEGIN_DOWN_GRACEFUL',
            'reset':'RESET',
            'operational':'OPERATIONAL',
            'not-operational':'NOT_OPERATIONAL',
            'unknown':'UNKNOWN',
            'last':'LAST',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuPerMonEnum' : _MetaInfoEnum('OtuPerMonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'disable':'DISABLE',
            'enable':'ENABLE',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuPpIntfStateEnum' : _MetaInfoEnum('OtuPpIntfStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'otu-pp-intf-up':'OTU_PP_INTF_UP',
            'otu-pp-intf-failing':'OTU_PP_INTF_FAILING',
            'otu-pp-intf-down':'OTU_PP_INTF_DOWN',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuPpFsmStateEnum' : _MetaInfoEnum('OtuPpFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'otu-in-active':'OTU_IN_ACTIVE',
            'otu-disabled':'OTU_DISABLED',
            'otu-normal-state':'OTU_NORMAL_STATE',
            'otu-local-failing':'OTU_LOCAL_FAILING',
            'otu-remote-failing':'OTU_REMOTE_FAILING',
            'otu-main-t-failing':'OTU_MAIN_T_FAILING',
            'otu-regen-failing':'OTU_REGEN_FAILING',
            'otu-local-failed':'OTU_LOCAL_FAILED',
            'otu-remote-failed':'OTU_REMOTE_FAILED',
            'otu-main-t-failed':'OTU_MAIN_T_FAILED',
            'otu-regen-failed':'OTU_REGEN_FAILED',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuTtiEtEnum' : _MetaInfoEnum('OtuTtiEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'ascii':'ASCII',
            'hex':'HEX',
            'full-ascii':'FULL_ASCII',
            'full-hex':'FULL_HEX',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuG709FecModeEnum' : _MetaInfoEnum('OtuG709FecModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'otu-bag-none-fec':'OTU_BAG_NONE_FEC',
            'otu-bag-standard-fec':'OTU_BAG_STANDARD_FEC',
            'otu-bag-1-i-7-fec':'OTU_BAG_1_I_7_FEC',
            'otu-bag-1-i-4-fec':'OTU_BAG_1_I_4_FEC',
            'otu-bag-swizzle-fec':'OTU_BAG_SWIZZLE_FEC',
            'otu-bag-hg20-fec':'OTU_BAG_HG20_FEC',
            'otu-bag-enhanced-hg7-fec':'OTU_BAG_ENHANCED_HG7_FEC',
            'otu-bag-sd20-fec':'OTU_BAG_SD20_FEC',
            'otu-bag-sd7-fec':'OTU_BAG_SD7_FEC',
            'otu-bag-all-fec':'OTU_BAG_ALL_FEC',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuSecStateEnum' : _MetaInfoEnum('OtuSecStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'normal':'NORMAL',
            'maintenance':'MAINTENANCE',
            'ais':'AIS',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuLoopBackModeEnum' : _MetaInfoEnum('OtuLoopBackModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'none':'NONE',
            'line':'LINE',
            'internal':'INTERNAL',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'GmplsOtuTtiModeEnum' : _MetaInfoEnum('GmplsOtuTtiModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'gmpls-otu-tti-mode-none':'GMPLS_OTU_TTI_MODE_NONE',
            'gmpls-otu-tti-mode-sm':'GMPLS_OTU_TTI_MODE_SM',
            'gmpls-otu-tti-mode-pm':'GMPLS_OTU_TTI_MODE_PM',
            'gmpls-otu-tti-mode-tcm':'GMPLS_OTU_TTI_MODE_TCM',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'OtuDerStateEnum' : _MetaInfoEnum('OtuDerStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper',
        {
            'out-of-service':'OUT_OF_SERVICE',
            'in-service':'IN_SERVICE',
            'maintenance':'MAINTENANCE',
            'ais':'AIS',
        }, 'Cisco-IOS-XR-controller-otu-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper']),
    'Otu.Controllers.Controller.Info.Local' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.Local',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                IfIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'local',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.Remote' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.Remote',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                IfIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'remote',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.TtiMode.Tx' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.TtiMode.Tx',
            False, 
            [
            _MetaInfoClassMember('dapi', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                exp String 
                ''',
                'dapi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('operator-specific', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rec String 
                ''',
                'operator_specific',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sapi', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                tx String 
                ''',
                'sapi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'tx',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.TtiMode.Exp' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.TtiMode.Exp',
            False, 
            [
            _MetaInfoClassMember('dapi', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                exp String 
                ''',
                'dapi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('operator-specific', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rec String 
                ''',
                'operator_specific',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sapi', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                tx String 
                ''',
                'sapi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'exp',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.TtiMode.Rec' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.TtiMode.Rec',
            False, 
            [
            _MetaInfoClassMember('dapi', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                exp String 
                ''',
                'dapi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('operator-specific', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rec String 
                ''',
                'operator_specific',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sapi', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 255)], [], 
                '''                tx String 
                ''',
                'sapi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'rec',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.TtiMode' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.TtiMode',
            False, 
            [
            _MetaInfoClassMember('exp', REFERENCE_CLASS, 'Exp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.TtiMode.Exp', 
                [], [], 
                '''                String Expected
                ''',
                'exp',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('g709tti-exp-mode', REFERENCE_ENUM_CLASS, 'OtuTtiEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuTtiEtEnum', 
                [], [], 
                '''                G709TTI Expected
                ''',
                'g709tti_exp_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('g709tti-rec-mode', REFERENCE_ENUM_CLASS, 'OtuTtiEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuTtiEtEnum', 
                [], [], 
                '''                G709TTI Recieved
                ''',
                'g709tti_rec_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('g709tti-sent-mode', REFERENCE_ENUM_CLASS, 'OtuTtiEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuTtiEtEnum', 
                [], [], 
                '''                G709TTI sent
                ''',
                'g709tti_sent_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('rec', REFERENCE_CLASS, 'Rec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.TtiMode.Rec', 
                [], [], 
                '''                String Received
                ''',
                'rec',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('tx', REFERENCE_CLASS, 'Tx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.TtiMode.Tx', 
                [], [], 
                '''                String Sent
                ''',
                'tx',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'tti-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Los' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Los',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'los',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'lof',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'lom',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'oof',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'oom',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'ais',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'iae',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'biae',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'bdi',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'tim',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'eoc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'fec-mismatch',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'sf-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'sd-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'ec',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'uc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'fecunc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.OtuAlarmInfo' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.OtuAlarmInfo',
            False, 
            [
            _MetaInfoClassMember('ais', REFERENCE_CLASS, 'Ais' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais', 
                [], [], 
                '''                Alarm Indication Signal
                ''',
                'ais',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('bdi', REFERENCE_CLASS, 'Bdi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi', 
                [], [], 
                '''                Backward Defect Indication
                ''',
                'bdi',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('biae', REFERENCE_CLASS, 'Biae' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae', 
                [], [], 
                '''                Backward Incoming Alignment Error
                ''',
                'biae',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('ec', REFERENCE_CLASS, 'Ec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec', 
                [], [], 
                '''                EC alarm
                ''',
                'ec',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('eoc', REFERENCE_CLASS, 'Eoc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc', 
                [], [], 
                '''                GCC End of Channel
                ''',
                'eoc',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('fec-mismatch', REFERENCE_CLASS, 'FecMismatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch', 
                [], [], 
                '''                FEC mismatch alarm
                ''',
                'fec_mismatch',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('fecunc', REFERENCE_CLASS, 'Fecunc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc', 
                [], [], 
                '''                FEC UnCorrected Word
                ''',
                'fecunc',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('iae', REFERENCE_CLASS, 'Iae' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae', 
                [], [], 
                '''                Incoming Alignment Error
                ''',
                'iae',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('lof', REFERENCE_CLASS, 'Lof' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof', 
                [], [], 
                '''                Loss of Frame
                ''',
                'lof',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('lom', REFERENCE_CLASS, 'Lom' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom', 
                [], [], 
                '''                Loss of MultiFrame
                ''',
                'lom',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('los', REFERENCE_CLASS, 'Los' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Los', 
                [], [], 
                '''                Loss of Signal
                ''',
                'los',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('oof', REFERENCE_CLASS, 'Oof' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof', 
                [], [], 
                '''                Out of Frame
                ''',
                'oof',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('oom', REFERENCE_CLASS, 'Oom' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom', 
                [], [], 
                '''                Out of MultiFrame
                ''',
                'oom',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sd-ber', REFERENCE_CLASS, 'SdBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer', 
                [], [], 
                '''                SD BER alarm
                ''',
                'sd_ber',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sf-ber', REFERENCE_CLASS, 'SfBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer', 
                [], [], 
                '''                SF BER alarm
                ''',
                'sf_ber',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('tim', REFERENCE_CLASS, 'Tim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim', 
                [], [], 
                '''                Trace Identifier Mismatch
                ''',
                'tim',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('uc', REFERENCE_CLASS, 'Uc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc', 
                [], [], 
                '''                UC alarm
                ''',
                'uc',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'otu-alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info.Proactive' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info.Proactive',
            False, 
            [
            _MetaInfoClassMember('proactive-fsm-if-state', REFERENCE_ENUM_CLASS, 'OtuPpIntfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPpIntfStateEnum', 
                [], [], 
                '''                Proactive FSM IF State
                ''',
                'proactive_fsm_if_state',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('proactive-fsm-state', REFERENCE_ENUM_CLASS, 'OtuPpFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPpFsmStateEnum', 
                [], [], 
                '''                Proactive FSM State
                ''',
                'proactive_fsm_state',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('proactive-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Proactive Status
                ''',
                'proactive_status',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('revert-window', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Revert Integration Window
                ''',
                'revert_window',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('rvrt-thresh-coeff', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Revert threshold coefficient
                ''',
                'rvrt_thresh_coeff',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('rvrt-thresh-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Revert threshold power
                ''',
                'rvrt_thresh_power',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sec-state', REFERENCE_ENUM_CLASS, 'OtuSecStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuSecStateEnum', 
                [], [], 
                '''                Secondary Admin State
                ''',
                'sec_state',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('trig-thresh-coeff', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Trigger threshold coefficient
                ''',
                'trig_thresh_coeff',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('trig-thresh-power', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Trigger threshold power
                ''',
                'trig_thresh_power',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('trigger-window', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Trigger Integration window
                ''',
                'trigger_window',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'proactive',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller.Info' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller.Info',
            False, 
            [
            _MetaInfoClassMember('derivedstate-mode', REFERENCE_ENUM_CLASS, 'OtuDerStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuDerStateEnum', 
                [], [], 
                '''                Derived State
                ''',
                'derivedstate_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('ec', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Average bit errors corrected
                ''',
                'ec',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('ec-value', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                EC value present
                ''',
                'ec_value',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('fec-mode', REFERENCE_ENUM_CLASS, 'OtuG709FecModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuG709FecModeEnum', 
                [], [], 
                '''                FEC
                ''',
                'fec_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('gcc-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OTU GCC
                ''',
                'gcc_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('gmpls-tti-mode', REFERENCE_ENUM_CLASS, 'GmplsOtuTtiModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'GmplsOtuTtiModeEnum', 
                [], [], 
                '''                GMPLS TTI MODE
                ''',
                'gmpls_tti_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('gmpls-tvm-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                GMPLS TCM ID
                ''',
                'gmpls_tvm_id',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('local', REFERENCE_CLASS, 'Local' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.Local', 
                [], [], 
                '''                TTI
                ''',
                'local',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('loopback-mode', REFERENCE_ENUM_CLASS, 'OtuLoopBackModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuLoopBackModeEnum', 
                [], [], 
                '''                Loopback
                ''',
                'loopback_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'name',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('network-srlg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Network SRLG
                ''',
                'network_srlg',
                'Cisco-IOS-XR-controller-otu-oper', False, max_elements=100),
            _MetaInfoClassMember('nv-optical-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NV Optical support
                ''',
                'nv_optical_support',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('otu-alarm-info', REFERENCE_CLASS, 'OtuAlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.OtuAlarmInfo', 
                [], [], 
                '''                OTU layer alarm Information
                ''',
                'otu_alarm_info',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('performance-monitoring', REFERENCE_ENUM_CLASS, 'OtuPerMonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuPerMonEnum', 
                [], [], 
                '''                Performance Monitoring
                ''',
                'performance_monitoring',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('pre-fec-ber-mantissa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pre fec val mantissa
                ''',
                'pre_fec_ber_mantissa',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('pre-fec-ber-value', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pre fec val present 
                ''',
                'pre_fec_ber_value',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('pre-fec-mantissa', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                Pre FEC BER Mantissa in form E-<mantisaa>
                ''',
                'pre_fec_mantissa',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('pre-fec-val', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Pre FEC BER Value in form 0.00
                ''',
                'pre_fec_val',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('proactive', REFERENCE_CLASS, 'Proactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.Proactive', 
                [], [], 
                '''                Proactive Protection
                ''',
                'proactive',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('q', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                q value calculated
                ''',
                'q',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('q-margin', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                q margin calculated
                ''',
                'q_margin',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('remote', REFERENCE_CLASS, 'Remote' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.Remote', 
                [], [], 
                '''                Remote
                ''',
                'remote',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sd', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                SD
                ''',
                'sd',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sec-state', REFERENCE_ENUM_CLASS, 'OtuSecStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuSecStateEnum', 
                [], [], 
                '''                Sec State
                ''',
                'sec_state',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('sf', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                SF
                ''',
                'sf',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'OtuStateEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'OtuStateEtEnum', 
                [], [], 
                '''                Admin State
                ''',
                'state',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('tti-mode', REFERENCE_CLASS, 'TtiMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info.TtiMode', 
                [], [], 
                '''                OTU TTI
                ''',
                'tti_mode',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('uc', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Uncorrected word count
                ''',
                'uc',
                'Cisco-IOS-XR-controller-otu-oper', False),
            _MetaInfoClassMember('uc-value', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Uc value present
                ''',
                'uc_value',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'controller_name',
                'Cisco-IOS-XR-controller-otu-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller.Info', 
                [], [], 
                '''                OTU port operational data
                ''',
                'info',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu.Controllers' : {
        'meta_info' : _MetaInfoClass('Otu.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers.Controller', 
                [], [], 
                '''                OTU Port operational data
                ''',
                'controller',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
    'Otu' : {
        'meta_info' : _MetaInfoClass('Otu',
            False, 
            [
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper', 'Otu.Controllers', 
                [], [], 
                '''                All OTU Port operational data
                ''',
                'controllers',
                'Cisco-IOS-XR-controller-otu-oper', False),
            ],
            'Cisco-IOS-XR-controller-otu-oper',
            'otu',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-otu-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_otu_oper'
        ),
    },
}
_meta_table['Otu.Controllers.Controller.Info.TtiMode.Tx']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.TtiMode.Exp']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.TtiMode.Rec']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Los']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lof']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Lom']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oof']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Oom']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ais']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Iae']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Biae']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Bdi']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Tim']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Eoc']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.FecMismatch']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SfBer']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.SdBer']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Ec']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Uc']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo.Fecunc']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.Local']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.Remote']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.TtiMode']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.OtuAlarmInfo']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info']['meta_info']
_meta_table['Otu.Controllers.Controller.Info.Proactive']['meta_info'].parent =_meta_table['Otu.Controllers.Controller.Info']['meta_info']
_meta_table['Otu.Controllers.Controller.Info']['meta_info'].parent =_meta_table['Otu.Controllers.Controller']['meta_info']
_meta_table['Otu.Controllers.Controller']['meta_info'].parent =_meta_table['Otu.Controllers']['meta_info']
_meta_table['Otu.Controllers']['meta_info'].parent =_meta_table['Otu']['meta_info']